# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
import shutil

sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath("../app"))

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
for filename in ["README.md", "CHANGELOG.md"]:
    src = os.path.join(base_dir, filename)
    dst = os.path.join(os.path.dirname(__file__), filename)
    if not os.path.exists(dst):
        shutil.copy(src, dst)


project = 'Books Management System'
copyright = '2025, Darshan D'
author = 'Darshan D'
release = '1.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser', 'sphinx.ext.todo', 'sphinx.ext.viewcode', 'sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
