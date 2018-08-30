#!/usr/bin/env python2
# -*- coding: utf-8 -*-


from setuptools import setup

import os
import sys
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'hackercodecs'))
import hackercodecs

setup(name="hackercodecs",
      version="0.3",
      description="A set of codecs for hackers",
      url="https://github.com/jdukes/hackercodecs",
      author="Josh Dukes",
      author_email="hex@neg9.org",
      license="MIT",
      keywords = "hacker, codecs, CTF",
      long_description=hackercodecs.__doc__,
      packages=["hackercodecs"])


# Copyright © 2012–2015 Josh Dukes <hex@neg9.org> and contributors.
#
# This is free software: you may copy, modify, and/or distribute this work
# under the terms of the Expat License.
# No warranty expressed or implied. See the file ‘LICENSE.Expat’ for details.

# Local variables:
# coding: utf-8
# End:
# vim: fileencoding=utf-8 filetype=python:
