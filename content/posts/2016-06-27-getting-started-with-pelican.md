title = "Getting Started with Pelican"
date = 2016-06-27T17:47:00+02:00
tags = [
    "pelican",
    "python",
    "getting",
    "started"
]
published = true
+++++

I am new to pelican, so in reality this is just the steps I used to setup my pelican blog. Feel free to experiment and do things differently.

### Create your virtual enviroment.

Anytime you are using python, you should always utilize a virtual enviroment. In this tutorial we will use virtualenv. This will prevent us from junking up our global install of python. 

For first timers I suggest visiting the hitchhiker's guide to python, as they have a very [comprehensive tutorial](http://docs.python-guide.org/en/latest/dev/virtualenvs/) on getting started with virtual enviroments.

### Install Pelican

Verify that your virtual enviroment is active so that we can start to install packages. Here we will install pelican and it's helper package Markdown.

```
pip install pelican Markdown
```

### Pelican Quick Start

Now it's time to setup the site. Run the quick-start command and enter in details such as the site name and description.

```
pelican-quickstart
```

*Note:* Make sure you decided on a catchy name!

### Pick a Theme

Pelican comes with a default theme, which I personally dislike. It just doesn't capture my personality very well. Luckily there is a site called [pelican themes](https://github.com/getpelican/pelican-themes) that will give us a good selection of 3rd party themes we can use on our site.

I personally really like the flex theme. Clone the theme of your choice and prep for your first blog post. Make sure you setup your `pelicanconf.py` file as deamed via the README in the themes repo.

### Create your first post

Write your first post in markdown and place it inside the `content` folder. 

### Compile your blog.

Time to have pelican generate your static HTML blog for you! Just run the command below. 

```
pelican
```

Simply upload your `output` folder and enjoy!