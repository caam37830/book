# Using Python

## The Python REPL (Read Evaluate Print Loop)

Assuming you have Python installed on your system, you can launch the REPL using the
`python` command in a terminal

```bash
(base) $ which python
~/miniconda3/bin/python
(base) $ conda activate pycourse
(pycourse) $ which python
~/miniconda3/envs/pycourse/bin/python
```

To launch the REPL:
```bash
(pycourse) $ python
Python 3.8.3 (default, Jul  2 2020, 16:21:59)
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

You can then enter commands in and hit `Enter` to run a command

```python
>>> print("hello world!")
hello world!
>>> 1 + 1
2
>>>
```

You can exit using the `exit()` function
```bash
>>> exit()
(pycourse) $
```

Alternatively, press `ctrl + d` to exit from terminal (this sends an end of file signal).

### ipython

A popular Python REPL with more features is packaged with [ipython](https://ipython.org/).

```bash
(pycourse) $ conda install ipython
(pycourse) $ ipython

Python 3.8.3 (default, Jul  2 2020, 16:21:59)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.18.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: 1 + 1
Out[1]: 2

In [2]:
```


## Python Scripts

Python scripts are text files stored with a `.py` extension.  You can run scripts from the command line

First, let's create a simple Python script which just prints a string:
```bash
(pycourse) $ echo 'print("hello world!")' > hello.py
```

You will now have a file `hello.py`
```bash
(pycourse) $ cat hello.py
print("hello world!")
```

You can run the script by executing `python hello.py`
```bash
(pycourse) $ python hello.py
hello world!
```

Here's a slightly more complex example.
```bash
(pycourse) $ cat script.py
"""
A simple python script
run from the terminal using
$ python script.py
"""

# printing will print to the terminal
print("hello world")

# you can do anything in your script
# define functions or classes
# import packages
# and so on...
def f(a, b):
    """
    returns the sum of a and b
    """
    return a + b

a = 1
b = 2
print(f"{a} + {b} = {f(a,b)}")
```

When we run the script:
```bash
(pycourse) $ python script.py
hello world
1 + 2 = 3
```
## Jupyter Notebooks

[Jupyter](https://jupyter.org/) (Julia, Python, R) notebooks mix code with markdown (a language for basic text formatting) in your browser.  This document is a Jupyter notebook, and the text is written in markdown.

### Installing Jupyter

First, launch a terminal, and [install notebooks](https://jupyter.org/install) **in your base environment**

```bash
(base) $ conda install -c conda-forge notebook
```
(`-c conda-forge` tells `conda` to install from the `conda-forge` channel).

### Test your installation

After installation, you should see a `jupyter` command is now available.

```bash
(base) $ which jupyter
~/miniconda3/bin/jupyter
```

### Install A Kernel for your environment

The next thing you need to do is install a kernel for your `pycourse` environment.  This will allow you to run code in Jupyter notebooks using the same setup as you would if you activate `pycourse`.

First, activate your `pycourse` environment in a terminal
```bash
(base) $ conda activate pycourse
(pycourse) $
```

Next, install the `ipykernel` package using `conda`
```bash
(pycourse) $ conda install ipykernel -c conda-forge
```

Now, you run the installation
```bash
(pycourse) $ python -m ipykernel install --user --name pycourse --display-name "Python (pycourse)"
```

Finally, deactivate your `pycourse` environment
```bash
(pycourse) $ conda deactivate
```

### Launch a Jupyter notebook server

Now, to launch a Jupyter notebook server, simply type
```bash
(base) $ jupyter notebook
```

You can launch the notebook server from any directory.

You can either create new notebooks, or launch existing notebooks.
