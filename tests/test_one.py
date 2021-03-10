# -*- coding=UTF-8 -*-
"""Tests for cast_unknown.one.  """

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import cast_unknown as cast


def test_none():
    assert cast.one(None) == None


def test_length_0():
    assert cast.one([]) == None


def test_length_1():
    assert cast.one([1]) == 1


def test_length_2():
    assert cast.one([1, 2]) == None


def test_generator():
    assert cast.one((i for i in (1,))) == 1


def test_infinite_generator():
    def _generator():
        while True:
            yield 1
    assert cast.one(_generator()) == None
