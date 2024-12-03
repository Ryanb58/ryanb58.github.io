A Simple Website Builder
------------------------

This is a website generator with support for pages, blog posts, and tag listings.

You write your content in markdown files and tag them with headers.

Configuration options are located in the `config.yml` file.


#### Requirements:

- [X] Write content in markdown
- [X] Control the URL structure for each post.
- [X] Generate a clickable list of blog posts.
- [X] Theme able?
- [ ] Generate a list of posts that share a specific tag.
- [ ] Configure main navigation via a file.


#### Sources:
https://dev.to/ritza/create-a-static-site-generator-with-python-and-replit-4bh6

## Using `uv`.

```
uv sync
uv run build.py
uv run python -m http.server -d docs/
```
