# -*- coding=UTF-8 -*-
"""tests for cast_unknown.instance.  """

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import pytest

import cast_unknown as cast


class Class1(object):
    pass


class Class2(Class1):
    pass


def test_match():
    obj1 = Class1()
    assert cast.instance(obj1, Class1) is obj1


def test_not_match():
    obj1 = Class1()
    cast.instance.__name__
    with pytest.raises(cast.CastError):
        cast.instance(obj1, Class2)


def test_match_tuple():
    obj1 = Class1()
    assert cast.instance(obj1, (Class1, Class2)) is obj1
