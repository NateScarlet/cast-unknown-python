# -*- coding=UTF-8 -*-
"""tests for cast_unknown.text.  """

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import cast_unknown as cast

from . import utils


def test_binary():
    assert cast.text(b"value") == "value"


def test_text():
    assert cast.text("测试") == "测试"


def test_utf8():
    assert cast.text(b'\xe6\xb5\x8b\xe8\xaf\x95') == "测试"


@utils.use_encoding("gbk")
def test_gbk():
    assert cast.text(b'\xb2\xe2\xca\xd4', "gbk") == "测试"


def test_int():
    assert cast.text(1) == "1"


def test_dict():
    assert cast.text(dict(a=1)) == "{'a': 1}"
