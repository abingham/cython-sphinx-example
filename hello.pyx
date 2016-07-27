def say_hello_to(name):
    "this is hello's docstring"
    print("Hello %s!" % name)


cdef int _eggs(unsigned long l, float f):
    return 3

def eggs(l, f, foo=None, *args, **kwargs):
    """Does something with eggs."""
    return _eggs(l, f)

cpdef fnord(int x, int y):
    """fnord fnord fnord"""
    return x + y
