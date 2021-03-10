# -*- coding=UTF-8 -*-
# pyright: reportMissingTypeStubs=none, reportUnknownVariableType=none,
"""Utils for test.  """

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import codecs

import pytest


def is_support_encoding(encoding):
    try:
        codecs.lookup(encoding)
        return True
    except LookupError:
        return False


def use_encoding(encoding):
    return pytest.mark.skipif(
        not is_support_encoding(encoding),
        reason="encoding not supported: %s" % encoding,
    )
