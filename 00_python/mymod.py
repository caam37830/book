"""
A simple Python module
"""

def plus1(x):
    """
    returns x + 1
    """
    return x + 1


class myclass:
    """
    simple class in a simple module
    """
    def __init__(self, a, b):
        self.a = a
        self.b = b


if __name__ == '__main__':
    print("mymod.py is being run as a script!")
    print("plus1(1) = {}".format(plus1(1)))
