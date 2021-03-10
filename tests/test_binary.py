# -*- coding=UTF-8 -*-
"""tests for cast_unknown.binary.  """

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import cast_unknown as cast

from . import utils


def test_binary():
    assert cast.binary(b"value") == b"value"


def test_text():
    assert cast.binary("测试") == b'\xe6\xb5\x8b\xe8\xaf\x95'


def test_utf8():
    assert cast.binary("测试", "utf-8") == b'\xe6\xb5\x8b\xe8\xaf\x95'


@utils.use_encoding("gbk")
def test_gbk():
    assert cast.binary("测试", "gbk") == b'\xb2\xe2\xca\xd4'


def test_int():
    assert cast.binary(1) == b"1"


def test_dict():
    assert cast.binary(dict(a=1)) == b"{'a': 1}"
