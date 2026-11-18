AUTHOR   = 'Geordanny'
SITENAME = "Geordanny's Blog"
SITEURL  = ""
THEME    = "./assets"

PATH = "content"

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM         = None
CATEGORY_FEED_ATOM    = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM      = None
AUTHOR_FEED_RSS       = None

# Blogroll
LINKS = [
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
]

# Social widget
SOCIAL = [
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
]

# This takes the name of the template, then filename/index.html  
TEMPLATE_PAGES = {
    'about.html' : 'about/index.html',
}

DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'posts')
POSTS_SAVE_AS = 'posts/index.html'
POSTS_URL = 'posts/'

PAGINATED_TEMPLATES = {
    'index'    : None,
    'tag'      : None,
    'category' : None,
    'author'   : None,
    'posts'    : None,
}

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
