This is a demonstration of how to use Cython's "embedsignature" compiler
directive to show Cython function signatures in Sphinx documentation. 
The main "magic" here is in `setup.py` where we actually specify the 
compiler directive.

First install the necessary requirements::

  pip install -r requirements.txt

To build the cython extension::

  python setup.py build_ext --inplace

Then build the sphinx docs::

  make clean && make html

The resulting documentations will be in `build/html/index.html`.
