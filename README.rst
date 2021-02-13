mmh3_unsigned
====

Python wrapper for MurmurHash (MurmurHash3), a set of fast and robust hash functions.

mmh3_unsigned 2.5.3 supports Python 3.3 and higher.

Usage
-----

Sample Usage::

    >>> import mmh3_unsigned
    >>> mmh3_unsigned.hash('foo') # 32 bit unsigned int
    -156908512
    >>> mmh3_unsigned.hash('foo', 42) # uses 42 for its seed
    -1322301282
    >>> mmh3_unsigned.hash('foo', signed=True) # 32 bit signed int (since Version 2.5)
    4138058784

Other functions::

    >>> mmh3_unsigned.hash64('foo') # two 64 bit signed ints (by using the 128-bit algorithm as its backend)
    (-2129773440516405919, 9128664383759220103)
    >>> mmh3_unsigned.hash64('foo',signed =False) #  two 64 bit unsigned ints
    (16316970633193145697, 9128664383759220103)
    >>> mmh3_unsigned.hash128('foo', 42) # 128 bit unsigned int
    215966891540331383248189432718888555506
    >>> mmh3_unsigned.hash128('foo', 42, signed = True) # 128 bit signed int
    -124315475380607080215185174712879655950
    >>> mmh3_unsigned.hash_bytes('foo') # 128 bit value as bytes
    'aE\xf5\x01W\x86q\xe2\x87}\xba+\xe4\x87\xaf~'

``hash64``, ``hash128``, and ``hash_bytes`` have the third argument for architecture optimization. Use True for x64 and False for x86 (default: True).::

    >>> mmh3_unsigned.hash64('foo', 42, True) 
    (-840311307571801102, -6739155424061121879)

Version 2.5 added ``hash_from_buffer``, which hashes byte-likes without memory copying. The method is suitable when you hash a large memory-view such as ``numpy.ndarray``.

    >>> mmh3_unsigned.hash_from_buffer(numpy.random.rand(100))
    -2137204694
    >>> mmh3_unsigned.hash_from_buffer(numpy.random.rand(100), signed = False)
    3812874078

Beware that ``hash64`` returns **two** values, because it uses the 128-bit version of MurmurHash3 as its backend.

Version 2.4 added support for 64-bit data.

    >>> import numpy as np
    >>> a = np.zeros(2**32, dtype=np.int8)
    >>> mmh3_unsigned.hash_bytes(a)
    b'V\x8f}\xad\x8eNM\xa84\x07FU\x9c\xc4\xcc\x8e'

Version 2.4 also changed the type of seeds from signed 32-bit int to unsigned 32-bit int. (**The resulting values with signed seeds still remain the same as before, as long as they are 32-bit**)

    >>> mmh3_unsigned.hash('aaaa', -1756908916) # signed rep. for 0x9747b28c
    1519878282
    >>> mmh3_unsigned.hash('aaaa', 2538058380) # unsigned rep. for 0x9747b28c
    1519878282

Be careful so that these seeds do not exceed 32-bit. Unexpected results may happen with invalid values.

    >>> mmh3_unsigned.hash('foo', 2 ** 33)
    -156908512
    >>> mmh3_unsigned.hash('foo', 2 ** 34)
    -156908512


Changes
=======
2.5.3 (2020-02-13)
* Changed to unsigned return value by default for compatibility with other hashing libraries in other languages

2.5.1 (2017-10-31)
------------------
* Bug fix for ``hash_bytes``. Thanks `doozr <https://github.com/doozr>`_!

2.5 (2017-10-28)
------------------
* Add ``hash_from_buffer``. Thanks `Dimitri Vorona <https://github.com/alendit>`_!
* Add a keyword argument ``signed``.

2.4 (2017-05-27)
------------------
* Support seeds with 32-bit unsigned integers; thanks `Alexander Maznev <https://github.com/pik>`_!
* Support 64-bit data (under 64-bit environments)
* Fix compile errors for Python 3.6 under Windows systems.
* Add unit testing and continuous integration with Travis CI and AppVeyor.

2.3.2 (2017-05-26)
------------------
* Relicensed from public domain to `CC0-1.0 <./LICENSE>`_.

2.3.1 (2015-06-07)
------------------
* Fix compile errors for gcc >=5.

2.3 (2013-12-08)
----------------
* Add ``hash128``, which returns a 128-bit signed integer.
* Fix a misplaced operator which could cause memory leak in a rare condition.
* Fix a malformed value to a Python/C API function which may cause runtime errors in recent Python 3.x versions.

The first two commits are from `Derek Wilson <https://github.com/underrun>`_. Thanks!

2.2 (2013-03-03)
----------------
* Improve portability to support systems with old gcc (version < 4.4) such as CentOS/RHEL 5.x. (Commit from `Micha Gorelick <https://github.com/mynameisfiber>`_. Thanks!)

2.1 (2013-02-25)
----------------

* Add `__version__` constant. Check if it exists when the following revision matters for your application.
* Incorporate the revision r147, which includes robustness improvement and minor tweaks.

Beware that due to this revision, **the result of 32-bit version of 2.1 is NOT the same as that of 2.0**. E.g.,::

    >>> mmh3_unsigned.hash('foo') # in mmh3_unsigned 2.0
    -292180858
    >>> mmh3_unsigned.hash('foo') # in mmh3_unsigned 2.1
    -156908512

The results of hash64 and hash_bytes remain unchanged. Austin Appleby, the author of Murmurhash, ensured this revision was the final modification to MurmurHash3's results and any future changes would be to improve performance only.

License
=======

`CC0-1.0 <./LICENSE>`_.

FAQ
===

How can I use this module? Any tutorials?
-----------------------------------------

The following textbooks and tutorials are great sources to learn how to use mmh3_unsigned (and other hash algorithms in general) for high-performance computing.

* Chapter 11: Using Less Ram in Micha Gorelick and Ian Ozsvald. 2014. *High Performance Python: Practical Performant Programming for Humans*. O'Reilly Media. `ISBN: 978-1-4493-6159-4 <https://www.amazon.com/dp/1449361595>`_.
* Duke University. `Efficient storage of data in memeory <http://people.duke.edu/~ccc14/sta-663-2016/20B_Big_Data_Structures.html>`_.
* Max Burstein. `Creating a Simple Bloom Filter <http://www.maxburstein.com/blog/creating-a-simple-bloom-filter/>`_.
* Bugra Akyildiz. `A Gentle Introduction to Bloom Filter <https://bugra.github.io/work/notes/2016-06-05/a-gentle-introduction-to-bloom-filter/>`_.

Some results are different from other MurmurHash3-based libraries.
------------------------------------------------------------------

By default, mmh3_unsigned returns **unsigned** values for 32-bit and 64-bit versions and **unsigned** values for ```hash128```, due to historical reasons. Please use the keyword argument ``signed`` to obtain a desired result.

For compatibility with Google Guava (Java), see https://stackoverflow.com/questions/29932956/murmur3-hash-different-result-between-python-and-java-implementation


I want to report errors/ask questions/send requests.
----------------------------------------------------

Thank you for helping me to improve the library. Please make sure to post them *through the issue tracking system of GitHub*. Issues sent directly to my email account may go unnoticed.

Authors
=======

MurmurHash3 was originally developed by Austin Appleby and distributed under public domain.

* https://code.google.com/p/smhasher/

Ported and modified for Python by Hajime Senuma.

Current modifications by Robert Palmer (robd003)

* https://pypi.python.org/pypi/mmh3_unsigned
* https://github.com/robd003/mmh3

See also
========

* https://github.com/wc-duck/pymmh3: mmh3 in pure python (Fredrik Kihlander and Swapnil Gusani)
* https://github.com/escherba/python-cityhash: Python bindings for CityHash (Eugene Scherba)
* https://github.com/veelion/python-farmhash: Python bindigs for FarmHash (Veelion Chong)
* https://github.com/escherba/python-metrohash: Python bindings for MetroHash (Eugene Scherba)
