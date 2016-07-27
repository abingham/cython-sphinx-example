First install the necessary requirements::

  pip install -r requirements.txt

To build the cython extension::

  python setup.py build_ext --inplace

Then build the sphinx docs::

  make clean && make html
