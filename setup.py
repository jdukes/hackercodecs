import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name="hackercodecs",
      version="0.1",
      description="A set of codecs for hackers",
      url="https://github.com/jdukes/hackercodecs",
      author="Josh Dukes",
      author_email="hex@neg9.org",
      license="MIT",
      keywords = "hacker, codecs, CTF",
      long_description=read('README.md'),
      packages=["hackercodecs"])
