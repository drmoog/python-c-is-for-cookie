========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis|
        |
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/python-c-is-for-cookie/badge/?style=flat
    :target: https://readthedocs.org/projects/python-c-is-for-cookie
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/drmoog/python-c-is-for-cookie.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/drmoog/python-c-is-for-cookie

.. |version| image:: https://img.shields.io/pypi/v/c-is-for-cookie.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/c-is-for-cookie

.. |commits-since| image:: https://img.shields.io/github/commits-since/drmoog/python-c-is-for-cookie/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/drmoog/python-c-is-for-cookie/compare/v0.1.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/c-is-for-cookie.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/c-is-for-cookie

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/c-is-for-cookie.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/c-is-for-cookie

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/c-is-for-cookie.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/c-is-for-cookie


.. end-badges

Testing out this package generator to see how it does them dastardly cffi bindings

* Free software: MIT license

Installation
============

::

    pip install c-is-for-cookie

Documentation
=============

https://python-c-is-for-cookie.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
