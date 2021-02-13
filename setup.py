# MurmurHash3 was written by Austin Appleby, and is placed in the public domain.
# mmh3 Python module was written by Hajime Senuma, and is also placed in the public domain.
# The authors hereby disclaim copyright to these source codes.

from setuptools import setup, Extension

mmh3module = Extension('mmh3_unsigned',
    sources = ['mmh3module.cpp', 'MurmurHash3.cpp'])

setup(name = 'mmh3_unsigned',
    version = '2.5.3',
    description = 'Python wrapper for MurmurHash (MurmurHash3), a set of fast and robust hash functions.',
    license = 'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
    author = 'Robert Palmer',
    author_email = 'rob@allfactors.com',
    url = 'http://packages.python.org/mmh3-unsigned',
    ext_modules = [mmh3module],
    keywords = "utility hash MurmurHash",
    long_description = open('README.rst').read(),
    classifiers = ['Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Topic :: Software Development :: Libraries',
    'Topic :: Utilities']
)
