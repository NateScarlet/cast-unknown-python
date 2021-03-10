# -*- coding=UTF-8 -*-
"""Tests for cast_unknown.datetime.  """

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import cast_unknown as cast
import datetime as dt
from dateutil import tz


def test_datetime():
    v = dt.datetime.now()
    assert cast.datetime(v) is v


def test_date():
    v = dt.date(2021, 3, 10)
    assert cast.datetime(v) == dt.datetime(2021, 3, 10,)


def test_time():
    assert cast.datetime_at(
        dt.time(12, 0, 0),
        dt.datetime(2021, 3, 10),
    ) == dt.datetime(2021, 3, 10, 12)


def test_isostring():
    assert cast.datetime("2021-03-10T00:00:00+08:00") == dt.datetime(
        2021,
        3,
        10,
        tzinfo=tz.tzstr("UTC+8")
    )


def test_isostring_date():
    assert cast.datetime("2021-03-10") == dt.datetime(
        2021,
        3,
        10,
    )


def test_isostring_time():
    assert cast.datetime_at("12:00", dt.datetime(2021, 3, 10)) == dt.datetime(
        2021,
        3,
        10,
        12,
    )


def test_isostring_bytes():
    assert cast.datetime(b"2021-03-10T00:00:00Z") == dt.datetime(
        2021,
        3,
        10,
        tzinfo=tz.UTC,
    )


def test_timestamp():
    assert cast.datetime(1615305600.0) == dt.datetime(
        2021,
        3,
        9,
        16,
    )


def test_timestamp_ms():
    assert cast.datetime(1615305600000) == dt.datetime(
        2021,
        3,
        9,
        16,
    )
