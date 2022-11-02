# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : wyy
# @file       :  __init__.py.py
# @Time    : 2021/10/26 9:44
# @Function:

"""
df =pandas.DataFrame()
print(df)
df =pandas.DataFrame([{"a":["q","w","e"]},{"b":["r","w","y"]}])
print("-----")
print(df)
df =df.append(pandas.DataFrame([{"a":["s","w","k"]},{"b":["h","b","f"]}]))
print("------")
print(df)

s="dss"
print(s.find("he"))

filename = 'foobar.txt'
basename, _, ext = filename.rpartition('.')
print(basename)
print(_)
print(ext)

tt=[1,2,3,4,5]
ll={"a":1}
a=ll
print(a)

def count():
    fs = []
    for i in range(1, 4):
        def g():
            a=i
            return a*a
        fs.append(g())

    return fs

d1,d2,d3=count()
print(d1,d2,d3)

def inc():
    x = 0
    def fn():
        nonlocal x
        x = x + 1
        return x
    return fn

f = inc()
print(f()) # 1
print(f()) # 2



x=1
y=2
f=lambda :x+y
f=f()
print(f)
def build(x, y):
    return lambda: x * x + y * y
f=build(2,3)
print(f())
kw = { 'base': 2 }
ii=int("10010", base= 2 )
print(ii )
def log(func):
    def wrapper(*args, **kw):
        print(*kw,kw)
        print(*args, args)

        print(f'call : %s(),arg : %s ， KW :{kw}'  % (func.__name__,*args ))
        return func(*args, **kw)
    return wrapper

@log
def now(s,**kw):  #log(now())
    print('2015-3-25')
    return "ddd"
ww=now
kw={"da":"ffd"}
print(ww("w",da="ff",c="ss"))


"""
