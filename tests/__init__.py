#!/usr/bin/env python2
from unittest import TestLoader
import doctest
import test_hackercodecs

from sys import path
path.append('../')
import hackercodecs


def HackerCodecsSuite():
    loader = TestLoader()
    suite = loader.loadTestsFromModule(test_hackercodecs)
    suite.addTests(doctest.DocTestSuite(hackercodecs))
    return suite
