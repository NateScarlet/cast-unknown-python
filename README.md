# cast-unknown-python

[![Action: Python package](https://github.com/NateScarlet/cast-unknown-python/actions/workflows/python-package.yml/badge.svg)](https://github.com/NateScarlet/cast-unknown-python/actions/workflows/python-package.yml)
![version](https://img.shields.io/pypi/v/cast-unknown)
![python versions](https://img.shields.io/pypi/pyversions/cast-unknown)
![wheel](https://img.shields.io/pypi/wheel/cast-unknown)

Cast unknown value to desired type with typing support.

Current supported cast target:

- text (unicode for python2, str for python3)
- binary (str for python2, bytes for python3)
- iterable
- datetime
- one (one and the only one item from given iterable, otherwise None)
- non_none (return default or raise error when given value is None)
- instance (raise error when not is instance)
- list (with optional item type check)

```python-repl
>>> import cast_unknown as cast
>>> import six
>>> cast.text('测试')
'测试'
>>> cast.text('测试'.encode('utf-8'))
'测试'
>>> cast.text(b'\xb2\xe2\xca\xd4', 'gbk')
'测试'
>>> cast.text(1)
'1'
>>> cast.text([])
'[]'
>>> cast.binary('测试')
b'\xe6\xb5\x8b\xe8\xaf\x95'
>>> cast.binary('测试'.encode('utf-8'))
b'\xe6\xb5\x8b\xe8\xaf\x95'
>>> cast.binary('测试', 'ascii')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "cast_unknown\binary.py", line 25, in binary
    return v.encode(encoding, errors)
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
>>> cast.binary('测试', 'gbk')
b'\xb2\xe2\xca\xd4'
>>> cast.binary([])
b'[]'
>>> cast.iterable(1)
[1]
>>> cast.iterable((i for i in (1,2,3)))
<generator object <genexpr> at 0x000000000220ECC8>
>>> cast.iterable([1])
[1]
>>> cast.iterable(None)
[]
>>> import datetime as dt
>>> cast.datetime(dt.datetime.now())
datetime.datetime(2021, 3, 10, 15, 27, 41, 69429)
>>> cast.datetime('2021-03-10T00:00:00+0800')
datetime.datetime(2021, 3, 10, 0, 0, tzinfo=tzoffset(None, 28800))
>>> cast.datetime('2021/03/10')
datetime.datetime(2021, 3, 10, 0, 0)
>>> cast.datetime(1615305600.0)
datetime.datetime(2021, 3, 9, 16, 0)
>>> cast.datetime(1615305600000)
datetime.datetime(2021, 3, 9, 16, 0)
>>> cast.one(1)
1
>>> cast.one(None)
None
>>> cast.one([1])
1
>>> cast.one([1,2])
None
>>> cast.not_none(1)
1
>>> cast.not_none(None)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "cast_unknown\not_none.py", line 14, in not_none
    raise CastError("value and default both None ")
cast_unknown.error.CastError: value and default both None
>>> cast.not_none(None, 1)
1
>>> cast.instance(1, int)
1
>>> cast.instance(1, str)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "cast_unknown\instance.py", line 23, in instance
    raise CastError(
cast_unknown.error.CastError: ('can not cast object to instance', 1, <class 'str'>)
>>> cast.instance(1, (str, int))
1
>>> cast.list_(None)
[]
>>> cast.list_([])
[]
>>> cast.list_(1)
[1]
>>> cast.list_([1])
[1]
>>> cast.list_([1], six.text_type)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "cast_unknown\list.py", line 14, in list_
    instance(i, class_or_tuple)
  File "cast_unknown\instance.py", line 23, in instance
    raise CastError(
cast_unknown.error.CastError: ('can not cast object to instance', 1, <class 'str'>)
>>> cast.list_([1], (int, six.text_type))
[1]
>>> cast.list_("abc")
['a', 'b', 'c']
>>> cast.list_("abc", six.text_type)
['abc']
```

## related

- [cast-unknown](https://github.com/NateScarlet/cast-unknown) for javascript
