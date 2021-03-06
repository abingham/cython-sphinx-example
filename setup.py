from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

# Compiler directives documentation
# https://github.com/cython/cython/wiki/enhancements-compilerdirectives

ext_modules = [Extension("cython_example", ["cython_example.pyx"])]

# This is the important part. By setting this compiler directive, cython will
# embed signature information in docstrings. Sphinx then knows how to extract
# and use those signatures.
for e in ext_modules:
    e.cython_directives = {"embedsignature": True}

setup(
    name='Demonstrating Sphinx function signatures for Cython modules',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules
)
