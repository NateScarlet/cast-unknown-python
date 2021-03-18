# -*- coding=UTF-8 -*-
"""Tests for cast_unknown.list_.  """

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import cast_unknown as cast

import pytest
import six


def test_none():
    assert cast.list_(None) == []


def test_type_not_match():
    with pytest.raises(cast.CastError, match="(u?'can not cast object to instance', None, <(class|type) 'int'>)"):
        cast.list_([1, None, 3], int)


def test_text():
    assert cast.list_("abc") == ["a", "b", "c"]


def test_text_with_type():
    assert cast.list_("abc", six.text_type) == ["abc"]


def test_iterator():
    assert cast.list_(six.moves.range(3)) == [0, 1, 2]
