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
