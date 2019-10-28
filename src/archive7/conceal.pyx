# cython: language_level=3
from archive7.archive cimport internal_print2


def test():
    internal_print()
    internal_print2()


cdef internal_print():
    print("Hello, world!")
