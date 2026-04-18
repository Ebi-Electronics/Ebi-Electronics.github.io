import os
import shutil
import subprocess
from pelican import signals

# Script to copy the output folder to docs, so that GitHub Pages can serve it from there
def copy_output_to_docs(sender):
    source = 'output'
    target = 'docs'
    if os.path.isdir(target):
        shutil.rmtree(target)
    shutil.copytree(source, target)
    # Build Pagefind search index inside output (and docs)
    subprocess.run(['python', '-m', 'pagefind', '--site', source], check=True)
    subprocess.run(['python', '-m', 'pagefind', '--site', target], check=True)

signals.finalized.connect(copy_output_to_docs)

AUTHOR = 'RDash'
SITENAME = 'Ebi Electronics'
SITEURL = ""
SITESUBTITLE = 'Another blog about electronics. Now with sea taste!'

PATH = "content"

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'EN'

THEME = 'themes/editoral'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Ebi Sound", "https://www.youtube.com/"),
    ("Ebi Electronics", "https://www.youtube.com/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

CONTACTS = [
    ("Twitter", "twitter", "https://twitter.com/theanalogfox"),
    ("Facebook", "facebook-f", "https://facebook.com/theanalogfox"),
    ("Instagram", "instagram", "https://www.instagram.com/theanalogfox/"),
    ("Email", "envelope", "info@theanalogfox.com"),
]

DEFAULT_PAGINATION = 10
PAGINATED_TEMPLATES = {'archives': None}

PLUGINS = ['render_math']
DELETE_OUTPUT_DIRECTORY = True

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
