# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import os
import sys
sys.path.insert(0, os.path.abspath('../src/ConfigureIt'))

# -- Project information -----------------------------------------------------

from datetime import date
project = 'ConfigureIt'
copyright = f'{date.today().year}, Arnav Das'
author = 'Arnav Das'

# The full version, including alpha/beta/rc tags
release = '0.1.0a0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',  # Core library for html generation from docstrings
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary',  # Create neat summary tables
]
autosummary_generate = True  # Turn on sphinx.ext.autosummary


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = 'pydata_sphinx_theme'
html_title = f"{project}"

html_theme_options = {
    "logo": {
        # "image_light": "logo.png",
        # "image_dark": "logo-dark.png",
        # "link": "<other page or external link>",
        # "text": f"{project}",
    },
    "github_url": "https://github.com/arnavdas88/ConfigureIt",
    "twitter_url": "https://twitter.com/arnavdas88",
    "show_prev_next": False,
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["theme-switcher", "navbar-icon-links", ],


    # "analytics_id": "G-XXXXXXXXXX",  #  Provided by Google in your dashboard
    # "analytics_anonymize_ip": False,

    # Toc options
    "show_toc_level": 1,
    "collapse_navigation": True,
    "show_nav_level": 1,
    "navigation_depth": 4,
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']