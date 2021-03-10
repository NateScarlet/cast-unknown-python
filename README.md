# cast-unknown-python

Cast unknown value to desired type with typing support.

Current supported cast target:

- text (unicode for python2, str for python3)
- binary (str for python2, bytes for python3)
- iterable
- datetime
- one (one and the only one item from given iterable, otherwise None)

```python-repl
>>> import cast_unknown as cast
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
```

## related

- [cast-unknown](https://github.com/NateScarlet/cast-unknown) for javascript
