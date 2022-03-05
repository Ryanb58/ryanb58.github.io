from livereload import Server, shell

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

server = Server()
server.watch('content', rerender_site)
server.serve(root='docs', port=8000, host='localhost')