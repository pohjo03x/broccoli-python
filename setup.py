#! /usr/bin/env python

import os
import sys

from distutils.core import setup, Extension

setup(name="broccoli-python", 
    version="1.71", # Filled in automatically.
    author_email="info@bro-ids.org",
    license="BSD",
    py_modules=['broccoli'],
    ext_modules = [ 
        Extension("_broccoli_intern", ["broccoli_intern_wrap.c"],
                  include_dirs=["../../src"],
                  library_dirs=["../../src/.libs"],
                  libraries=["broccoli"])]
)

