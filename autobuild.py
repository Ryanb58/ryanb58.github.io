from livereload import Server

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

theme_to_watch = load_config("config.toml").get("theme")
server = Server()
server.watch("content/**/*.md", rerender_site)
server.watch("themes/{}".format(theme_to_watch), rerender_site)
server.setHeader('Access-Control-Allow-Origin', '*')
server.setHeader('Access-Control-Allow-Methods', '*')
server.serve(
    root='docs', 
    port=8000,
    liveport=8001, 
    host='localhost',
    restart_delay=5
)