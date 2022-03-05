import distutils.dir_util
import glob
import os
import pathlib
import re
import shutil

import inflect
import jinja2
import markdown
import toml



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
            item["content"] = markdown.markdown(content, extensions=['nl2br','tables', 'fenced_code'])
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


def load_templates(template_directory):
    file_system_loader = jinja2.FileSystemLoader(template_directory)
    return jinja2.Environment(loader=file_system_loader)


def render_site(config, content, environment, output_directory):
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
    os.mkdir(output_directory)

    for content_type in config["types"]:  # <-- new for loop
        render_type(content_type)

    # Homepage
    index_template = environment.get_template("index.html")
    with open(f"{output_directory}/index.html", "w") as file:
        file.write(index_template.render(config=config, content=content))

    # Static files from theme
    distutils.dir_util.copy_tree(
        "themes/{}/static".format(config.get("theme")), output_directory
    )

    # Static files from content
    if os.path.exists("content/static"):
        distutils.dir_util.copy_tree(
            "content/static".format(config.get("theme")), f"{output_directory}"
        )
