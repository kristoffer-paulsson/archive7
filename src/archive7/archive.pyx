# cython: language_level=3
def test2():
    internal_print2()

cdef internal_print2():
    print("Hello, universe!")
