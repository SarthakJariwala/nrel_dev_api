"""Sphinx configuration."""
from datetime import datetime


project = "NREL Dev API"
author = "Sarthak Jariwala"
copyright = f"2020 - {datetime.now().year}, {author}"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]
autodoc_typehints = "description"
html_theme = "sphinx_book_theme"
