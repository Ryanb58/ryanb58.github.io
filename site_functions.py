import distutils.dir_util
import glob
import os
import pathlib
import re
import shutil
from datetime import datetime

import inflect
import jinja2
import markdown
import toml
from shutil import copytree, ignore_patterns
from feedgenerator import Rss201rev2Feed

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []

    def handle_data(self, data):
        self.text.append(data)

    def get_text(self):
        return ''.join(self.text).lstrip()

def remove_html_tags(text):
    parser = MyHTMLParser()
    parser.feed(text)
    return parser.get_text()

# # Test the function
# html_text = "<p>This is <em>an example</em> string.</p>"
# result = remove_html_tags(html_text)
# print(result)  # Output: "This is an example string."


def load_config(config_filename):

    with open(config_filename, "r") as config_file:
        config = toml.loads(config_file.read())

    ie = inflect.engine()
    for content_type in config["types"]:
        config[content_type]["plural"] = ie.plural(content_type)

    return config


def load_content_items(config, content_directory):
    def load_content_type(content_type):
        items = []
        for fn in glob.glob(
            f"{content_directory}/{config[content_type]['plural']}/*.md"
        ):
            with open(fn, "r") as file:
                frontmatter, content = re.split(
                    "^\+\+\+\+\+$", file.read(), 1, re.MULTILINE
                )

            item = toml.loads(frontmatter)
            item["content_stripped_of_html"] = remove_html_tags(content)
            item["content"] = markdown.markdown(content, extensions=['nl2br','tables', 'fenced_code', 'pymdownx.magiclink'])
            item["slug"] = os.path.splitext(os.path.basename(file.name))[0]
            if config[content_type]["dateInURL"]:
                item[
                    "url"
                ] = f"/{item['date'].year}/{item['date'].month:0>2}/{item['date'].day:0>2}/{item['slug']}/"
            else:
                item["url"] = f"/{item['slug']}/"

            # BY DEFAULT: ONLY LOAD PUBLISHED CONTENT
            if item["published"]:
                items.append(item)
            else:
                print("skipped draft: {}".format(item["slug"]))

        # sort according to config
        items.sort(
            key=lambda x: x[config[content_type]["sortBy"]],
            reverse=config[content_type]["sortReverse"],
        )

        return items

    content_types = {}
    for content_type in config["types"]:
        content_types[config[content_type]["plural"]] = load_content_type(content_type)

    # Group posts by year, so we can display them easier on the FE.
    from itertools import groupby
    # sort posts by date descending first
    # should be done with database query, but here's how otherwise
    posts = content_types["posts"]
    posts = sorted(posts, key=lambda post: post.get("date"), reverse=True)
    posts_grouped_by_date = groupby(posts, key=lambda post: post.get("date").year)
    content_types["posts_grouped_by_year"] = posts_grouped_by_date

    return content_types


def generate_rss_feed(content):
    """Using the data passed in, generate an RSS feed."""

    def truncate_at_word(input_string, max_length):
        if len(input_string) <= max_length:
            return input_string
        else:
            truncated = input_string[:max_length]
            return truncated[:truncated.rfind(' ')]

    # Initialize the feed
    feed = Rss201rev2Feed(
        title="Taylor Brazelton's Blog",
        link="https://taylorbrazelton.com",
        description="Updates and posts from Taylor Brazelton",
        language="en",
    )
    blog_posts = content["posts"]
    # Populate the feed with items (blog posts)
    for post in blog_posts:
        feed.add_item(
            title=post['title'],
            link=f"https://taylorbrazelton.com{post['url']}",
            description=truncate_at_word(post['content_stripped_of_html'], 128),
            pubdate=post['date']
        )

    # Generate RSS feed as a string
    rss_output = feed.writeString('utf-8')
    return rss_output


def load_templates(template_directory):
    file_system_loader = jinja2.FileSystemLoader(template_directory)
    return jinja2.Environment(loader=file_system_loader)


def render_site(config, content, environment, output_directory):

    # Rewrite the output directory to include the static prefix.
    def render_type(content_type):  # <-- new inner function
        # Post pages
        template = environment.get_template(f"{content_type}.html")
        for item in content[config[content_type]["plural"]]:
            path = f"{output_directory}/{item['url']}"
            pathlib.Path(path).mkdir(parents=True, exist_ok=True)
            with open(path + "index.html", "w") as file:
                file.write(template.render(this=item, config=config, content=content))

    if os.path.exists(output_directory):
        shutil.rmtree(output_directory)
    os.makedirs(output_directory + "/static", exist_ok=True)

    for content_type in config["types"]:  # <-- new for loop
        render_type(content_type)

    # CNAME Record:
    with open(f"{output_directory}/CNAME", "w") as file:
        file.write("taylorbrazelton.com")

    # RSS & Atom Feeds
    os.makedirs(output_directory + "/feed", exist_ok=True)
    with open(output_directory + "/feed/rss.xml", 'w', encoding='utf-8') as f:
        rss_output = generate_rss_feed(content)
        f.write(rss_output)

    # Homepage
    index_template = environment.get_template("index.html")
    with open(f"{output_directory}/index.html", "w") as file:
        file.write(index_template.render(config=config, content=content))

    # Static files from theme
    copytree(
        "themes/{}/static".format(config.get("theme")), 
        f"{output_directory}/static", 
        dirs_exist_ok=True, 
        ignore=ignore_patterns('*.pyc', '*.txt', '.DStore')
    )

    # distutils.dir_util.copy_tree(
    #     "themes/{}/static".format(config.get("theme")), f"{output_directory}/static"
    # )

    # Static files from content
    if os.path.exists("content/static"):
        copytree(
            "content/static",
            f"{output_directory}/static", 
            dirs_exist_ok=True, 
            ignore=ignore_patterns('*.pyc', '*.txt', '.DStore')
        )
        # distutils.dir_util.copy_tree(
        #     "content/static", f"{output_directory}/static"
        # )
