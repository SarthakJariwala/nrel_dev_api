"""Sphinx configuration."""
from datetime import datetime


project = "nrel-dev-api : Python API to access data and analysis services from NREL (National Renewable Energy Lab)"
author = "Sarthak Jariwala"
copyright = f"2020 - {datetime.now().year}, {author}"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
]

autodoc_typehints = "description"
autoclass_content = "both"

html_theme = "sphinx_book_theme"

html_theme_options = {
    "repository_url": "https://github.com/SarthakJariwala/nrel_dev_api",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "path_to_docs": "docs",
    "use_download_button": True,
    "use_fullscreen_button": True,
    # "extra_navbar": "<p>Your HTML</p>"
}
html_title = "nrel-dev-api"
