title = "Docker Image Size Reduction"
date = 2021-01-05T17:47:00+02:00
tags = [
    "docker",
    "image",
    "size",
    "reduction"
]
published = true
+++++

Recently I needed to dockerize an application for a virtual onprem. However, at the end of my project I ended up with a docker image that was 8.4 GB. This is HUGE in terms of size for a container. Thus, I went on a short journey to minimize the image using the following techniques.

1) Prevent APT from installing recommended packages by adding the following parameter to every apt-get install command: `--no-install-recommends`.

2) Added a `.dockerignore` file. This allows one to define a list of folders/file globs to ignore when building your Dockerfile.

3) Reduced the amount of layers by merging related commands.

4) Clean up apt cache via: `&& rm -rf /var/lib/apt/lists/*`.

5) Used [dive](https://github.com/wagoodman/dive) to inspect my image layers to analyze and remove extra unused packages/files.

6) I stumbled across a tool [docker-slim](https://github.com/docker-slim/docker-slim) that can supposedly reduce a container's size by up to 30x.

7) Check your base image. Think about running an alpine version of the container if you haven't already.

8) Use multistage builds.

9) Use your layers wisely. Put commands that are more likely to change towards the bottom.

10) Lint your dockerfile using [FromLatest](https://www.fromlatest.io/)

#### Sources:
- https://ubuntu.com/blog/we-reduced-our-docker-images-by-60-with-no-install-recommends
- https://towardsdatascience.com/slimming-down-your-docker-images-275f0ca9337e

Originally Posted on [dev.to](https://dev.to/mrbrazel/docker-image-size-reduction-220a)