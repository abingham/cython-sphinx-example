def cython_example(name):
    "An example in cython."
    print("Hello %s!" % name)


cdef int _cython_example_2(unsigned long l, float f):
    return 3

def cython_example_2(l, f, foo=None, *args, **kwargs):
    """Another cython example."""
    return _cython_example_2(l, f)

cpdef cython_cpdef_example(int x, int y):
    """A cython example using cpdef."""
    return x + y
