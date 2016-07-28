Cython function signatures in Sphinx
====================================

This is a demonstration of how to use Cython's ``embedsignature`` compiler
directive to show Cython function signatures in Sphinx documentation. 
The main "magic" here is in ``setup.py`` where we actually specify the 
compiler directive.

The demonstration involves creating a Cython-based module along with a 
pure Python module and then rendering their documentation in Sphinx via 
``autodoc``. The Sphinx-generated HTML contains function signature 
information for both the pure Python functions as well as those defined 
in Cython.

Running the demo
----------------

First install the necessary requirements::

  pip install -r requirements.txt

To build the cython extension::

  python setup.py build_ext --inplace

Then build the sphinx docs::

  make clean && make html

The resulting documentations will be in `build/html/index.html`.
