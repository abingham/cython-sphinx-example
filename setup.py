from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

# Compiler directives documentation
# https://github.com/cython/cython/wiki/enhancements-compilerdirectives

ext_modules = [Extension("hello", ["hello.pyx"])]

for e in ext_modules:
    e.cython_directives = {"embedsignature": True}

setup(
    name='Hello world app',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules
)
