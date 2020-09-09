Scientific Computing with Python
CAAM 37380 = STATS 37380

This is a course reader/book created using [Jupyter Book](https://jupyterbook.org/intro.html)

to build the book,
```
cd ..
jupyter-book build book
```

If you're running a custom jupyter kernel, you'll need to install it:
```
python -m ipykernel install --user --name pycourse --display-name "Python (pycourse)"
```

To publish to github pages, the `ghp-import` package is used.
See this link:
https://jupyterbook.org/publish/gh-pages.html#push-your-book-to-a-branch-hosted-by-github-pages
From the root of this repository:
```bash
ghp-import -n -p -f _build/html
```
