# -*- coding: utf-8 -*-
#
# This file is part of cortosis.
#
# Copyright (C) 2025 Interstellio IO (PTY) LTD.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import multiprocessing
import os
import sys

try:
    import sphinx_rtd_theme   # noqa: F401
    html_theme = "sphinx_rtd_theme"
except ImportError:
    html_theme = 'default'

sys.path.insert(0, os.path.abspath('..'))

from cortosis import metadata  # noqa: E402

# -- Build tweaks -------------------------------------------------------------

if not sys.platform.startswith('win'):
    multiprocessing.set_start_method('fork')

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('.'))

# -- Project information ------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

_version_components = metadata.version.split('.')

project = metadata.project_no_spaces
copyright = metadata.copyright
author = metadata.author
version = '.'.join(_version_components[0:3])
release = version

# -- General configuration ----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

if html_theme == 'sphinx_rtd_theme':
    extensions.append('sphinx_rtd_theme')

templates_path = ['_templates']
exclude_patterns = ['_build', '_newsfragments']

# Intersphinx configuration
intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}

# -- Options for HTML output --------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_show_sourcelink = False
html_favicon = '_static/favicon.png'
html_logo = '_static/logo.png'
html_static_path = ['_static']

# Theme options are theme-specific and customize the look and feel further.
# https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/index.html

html_theme_options = {
}
