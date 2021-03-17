# -*- coding=UTF-8 -*-
"""tests for cast_unknown.iterable.  """

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import cast_unknown as cast
import inspect


def test_none():
    assert cast.iterable(None) == []


def test_list():
    assert cast.iterable([1, 2, 3]) == [1, 2, 3]


def test_text():
    assert cast.iterable("abc") == "abc"


def test_binary():
    assert cast.iterable(b"abc") == b"abc"


def test_generator():
    it = cast.iterable((i for i in (1, 2, 3)))
    assert inspect.isgenerator(it)
    for index, i in enumerate(it):
        assert i == (1, 2, 3)[index]


def test_object():
    v = object()
    it = cast.iterable(v)
    for index, i in enumerate(it):
        assert i is (v,)[index]
