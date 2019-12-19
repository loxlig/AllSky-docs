# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license - see LICENSE.rst
#
# Astropy shared Sphinx settings.  These settings are shared between
# astropy itself and affiliated packages.
#
# Note that not all possible configuration values are present in this file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
import warnings
from os import path

import sphinx
from distutils.version import LooseVersion

# Must keep copy of source files in /home/sel/documentation/*.py
# in addition to the same files located in /home/sel/documentation/AllSky

# sys.path.insert(0, os.path.abspath('.'))
# sys.path.append('.')


# -- General configuration ----------------------------------------------------

# The version check in Sphinx itself can only compare the major and
# minor parts of the version number, not the micro.  To do a more
# specific version check, call check_sphinx_version("x.y.z.") from
# your project's conf.py
needs_sphinx = '1.7'


on_rtd = os.environ.get('READTHEDOCS', None) == 'True'


def check_sphinx_version(expected_version):
    sphinx_version = LooseVersion(sphinx.__version__)
    expected_version = LooseVersion(expected_version)
    if sphinx_version < expected_version:
        raise RuntimeError(
            "At least Sphinx version {0} is required to build this "
            "documentation.  Found {1}.".format(
                expected_version, sphinx_version))


# Configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/',
               (None, 'http://data.astropy.org/intersphinx/python3.inv')),
    'pythonloc': ('http://docs.python.org/',
                  path.abspath(path.join(path.dirname(__file__), '..',
                                         'local', 'python3_local_links.inv'))),
    'numpy': ('https://docs.scipy.org/doc/numpy/',
              (None, 'http://data.astropy.org/intersphinx/numpy.inv')),
    'scipy': ('https://docs.scipy.org/doc/scipy/reference/',
              (None, 'http://data.astropy.org/intersphinx/scipy.inv')),
    'matplotlib': ('https://matplotlib.org/',
                   (None, 'http://data.astropy.org/intersphinx/matplotlib.inv')),
    'astropy': ('http://docs.astropy.org/en/stable/', None),
    'h5py': ('http://docs.h5py.org/en/stable/', None)}

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# The reST default role (used for this markup: `text`) to use for all
# documents. Set to the "smart" one.
default_role = 'obj'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# This is added to the end of RST files - a good place to put substitutions to
# be used globally.
#rst_epilog = """
#.. _Astropy: https://www.astropy.org
#"""

suppress_warnings = ['app.add_directive', ]

# -- Project information ------------------------------------------------------

project = 'allsky'
copyright = '2019, Len Bright'
author = 'Len Bright'

# The short X.Y version
version = '0.1'
# The full version, including alpha/beta/rc tags
release = '1.0.5'


# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
#pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Settings for extensions and extension options ----------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
#    'sphinx_astropy.ext.intersphinx_toggle',
#    'sphinx.ext.intersphinx',
#    'sphinx.ext.inheritance_diagram',
#     'sphinx_automodapi.automodapi',
#    'sphinx_automodapi.smart_resolver',

extensions = [
    'sphinx.ext.autodoc',
    # 'sphinx_automodapi.automodapi',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'numpydoc',
    # 'sphinx_astropy.ext.doctest',
    # 'sphinx_astropy.ext.changelog_links',
    # 'sphinx_astropy.ext.missing_static',
    'sphinx.ext.mathjax']

# try:
#    import matplotlib.sphinxext.plot_directive
#    extensions += [matplotlib.sphinxext.plot_directive.__name__]
# AttributeError is checked here in case matplotlib is installed but
# Sphinx isn't.  Note that this module is imported by the config file
# generator, even if we're not building the docs.
# except (ImportError, AttributeError):
#    warnings.warn(
#        "matplotlib's plot_directive could not be imported. " +
#        "Inline plots will not be included in the output")

# Don't show summaries of the members in each class along with the
# class' docstring
numpydoc_show_class_members = False

autosummary_generate = True

# automodapi_toctreedirnm = 'api'

# Class documentation should contain *both* the class docstring and
# the __init__ docstring
autoclass_content = "both"

# Render inheritance diagrams in SVG
graphviz_output_format = "svg"

graphviz_dot_args = [
    '-Nfontsize=10',
    '-Nfontname=Helvetica Neue, Helvetica, Arial, sans-serif',
    '-Efontsize=10',
    '-Efontname=Helvetica Neue, Helvetica, Arial, sans-serif',
    '-Gfontsize=10',
    '-Gfontname=Helvetica Neue, Helvetica, Arial, sans-serif'
]

inheritance_node_attrs = dict(shape='ellipse', fontsize=9, height=0.75)

inheritance_graph_attrs = dict(rankdir="LR", size='"6.0, 8.0"',
                               fontsize=14, ratio='compress')


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'bootstrap-astropy'

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    '**': ['localtoc.html'],
    'search': [],
    'genindex': [],
    'py-modindex': [],
}

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.

# We include by default the favicon that is in the bootstrap-astropy theme.
import astropy_sphinx_theme
html_theme_path = astropy_sphinx_theme.get_html_theme_path()
html_favicon = os.path.join(html_theme_path[0], html_theme, 'static', 'astropy_logo.ico')

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%d %b %Y'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# -- Options for LaTeX output ------------------------------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
latex_toplevel_sectioning = 'part'

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

latex_elements = {}

# Additional stuff for the LaTeX preamble.
latex_elements['preamble'] = r"""
% Use a more modern-looking monospace font
\usepackage{inconsolata}

% The enumitem package provides unlimited nesting of lists and enums.
% Sphinx may use this in the future, in which case this can be removed.
% See https://bitbucket.org/birkenfeld/sphinx/issue/777/latex-output-too-deeply-nested
\usepackage{enumitem}
\setlistdepth{15}

% In the parameters section, place a newline after the Parameters
% header.  (This is stolen directly from Numpy's conf.py, since it
% affects Numpy-style docstrings).
\usepackage{expdlist}
\let\latexdescription=\description
\def\description{\latexdescription{}{} \breaklabel}

% Support the superscript Unicode numbers used by the "unicode" units
% formatter
\DeclareUnicodeCharacter{2070}{\ensuremath{^0}}
\DeclareUnicodeCharacter{00B9}{\ensuremath{^1}}
\DeclareUnicodeCharacter{00B2}{\ensuremath{^2}}
\DeclareUnicodeCharacter{00B3}{\ensuremath{^3}}
\DeclareUnicodeCharacter{2074}{\ensuremath{^4}}
\DeclareUnicodeCharacter{2075}{\ensuremath{^5}}
\DeclareUnicodeCharacter{2076}{\ensuremath{^6}}
\DeclareUnicodeCharacter{2077}{\ensuremath{^7}}
\DeclareUnicodeCharacter{2078}{\ensuremath{^8}}
\DeclareUnicodeCharacter{2079}{\ensuremath{^9}}
\DeclareUnicodeCharacter{207B}{\ensuremath{^-}}
\DeclareUnicodeCharacter{00B0}{\ensuremath{^{\circ}}}
\DeclareUnicodeCharacter{2032}{\ensuremath{^{\prime}}}
\DeclareUnicodeCharacter{2033}{\ensuremath{^{\prime\prime}}}

% Make the "warning" and "notes" sections use a sans-serif font to
% make them stand out more.
\renewenvironment{notice}[2]{
  \def\py@noticetype{#1}
  \csname py@noticestart@#1\endcsname
  \textsf{\textbf{#2}}
}{\csname py@noticeend@\py@noticetype\endcsname}
"""

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# -- Options for the linkcheck builder ----------------------------------------

# A timeout value, in seconds, for the linkcheck builder
linkcheck_timeout = 60
