# Packages and Setup

We have seen how you can write your own libraries and packages of code and import them when they are in the same folder as a script.  What if you want to be able to import your code from any location by installing it to your Python packages?

```python
import mypack
```

You can do all this using a file called `setup.py` and the `setuptools` Python package.

## Package Structure

There is a bit of variation in how Python packages are structured in practice.  We'll talk about one option, which is fairly standard for low-complexity projects.  Let's say your Python package is called `mypack`.  All the source materials for your package (including code, documentation, tests...) should be contained in a single folder, ideally a `git` repository.  One example is the package in the [python-packages repository](https://github.com/caam37830/python-packages).

Inside this top-level folder, you will have several sub-folders and files:
* `mypack` - the folder containing `__init__.py` which is your Python package source code.
* `doc` - folder which holds documentation for your package.
* `tests` folder, or `test.py` - code for testing your package (unit tests).
* `requirements.txt` - dependencies of your package (e.g. numpy, scipy, etc.)
* `setup.py` - a Python script used to configure and automate your package installation
* `LICENSE` - a license for people who use your code.  See [choosealicence.com](https://choosealicense.com/) for help choosing a license for your original work.  If your code is based on someone else's you will probably need to keep their license.
* `README.md` - a file that contains all the information people should read before installing/using your package.

There may be additional files as well (e.g. `.git`, files for CI, etc.) the above list is not exhaustive.

### requirements.txt

This is a file which lists dependencies of your package.  You can list packages without version numbers, or use some version specifiers
```
matplotlib # no version number
numpy >= 1.18 # must be version 1.18 or later
scipy >= 1.5 # must be version 1.5 or later
```

You can install requirements using `conda`:
```
conda install --file requirements.txt
```

or `pip`:
```
pip install -r requirements.txt
```

### setup.py

This is a file that is used to configure and install your repository to your Python path.  From the root of your repository, you should be able to run
```
pip install .
```
to install the code to your Python path.  You can then use `mypack` anywhere - not just in the directory that contains the source code.

In order to uninstall your package, you can run
```
pip uninstall mypack
```

You can also run `setup.py` as a script:

```
python setup.py install
```

In general, you'll want to use the `setuptools` package.  Basic useage is to use `setuptools.setup`, which accepts a variety of keyword arguments that help build and describe your package.  See [here](https://packaging.python.org/tutorials/packaging-projects/#creating-setup-py) for more details.
* `name`: your package name (`name='mypack'` in this case)
* `packages`: the actual package source code location (`packages=['mypack']`)
