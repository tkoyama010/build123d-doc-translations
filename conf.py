# basedir is set by <lang>/conf.py
"""
Use "-D language=<LANG>" option to build a localized build123d-docs document.
For example::

    sphinx-build -D language=ja -b html . _build/html

This conf.py does:

- Specify `locale_dirs`.
- Overrides source directory as `build123d/docs`.

"""
import os
import pathlib

basedir = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "build123d/docs"
)
exec(pathlib.Path(os.path.join(basedir, "conf.py")).read_text(), globals())
locale_dirs = [os.path.join(basedir, "../../locale/")]


def setup(app):
    app.srcdir = basedir
    app.confdir = app.srcdir
