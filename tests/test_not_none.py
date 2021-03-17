# -*- coding=UTF-8 -*-
"""Tests for cast_unknown.one.  """

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from cast_unknown.error import CastError

import cast_unknown as cast

import pytest


def test_none():
    with pytest.raises(CastError):
        cast.not_none(None)


def test_none_with_default():
    assert cast.not_none(None, 1) == 1


def test_not_none():
    assert cast.not_none(1) == 1


def test_not_none_with_default():
    assert cast.not_none(1, 2) == 1
