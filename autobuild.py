from livereload import Server
import os

from site_functions import load_config
from site_functions import load_content_items
from site_functions import load_templates
from site_functions import render_site


def rerender_site():
    config = load_config("config.toml")
    content = load_content_items(config, "content")
    environment = load_templates("themes/{}".format(config.get("theme")))
    output_folder = config.get("outputFolder", "public")
    render_site(config, content, environment, output_folder)


def standard_files_to_ignore(filename):
    _, ext = os.path.splitext(filename)
    return ext in [".pyc", ".pyo", ".o", ".swp", ".DStore"]


server = Server()

server.watch("content/**/*.md", rerender_site, ignore=standard_files_to_ignore)
server.watch("themes/**/*.*", rerender_site, ignore=standard_files_to_ignore)

server.setHeader("Access-Control-Allow-Origin", "*")
server.setHeader("Access-Control-Allow-Methods", "*")

server.serve(root="docs", port=8000, host="localhost", restart_delay=2, live_css=False)
