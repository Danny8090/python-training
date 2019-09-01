#!/usr/bin/env python
# coding=utf-8

"""
@author: danny ding
@license: MIT
@contact: goufaner520@outlook.com
@software: Python
@file: 05-yield关键字.py
@time: 2019/9/1 17:30
@desc: Python中还有另外一种定义生成器的方式，就是通过yield关键字将一个普通函数改造成生成器函数

"""

"""
斐波拉切数列的生成器,所谓斐波拉切数列可以通过下面递归的方法来进行定义：
f(0) = 0
f(1) = 1
f(n) = f(n-1) + f(n-2)(n>=2)
"""


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main(n):
    for val in fib(n):
        print(val, end=' ')


if __name__ == '__main__':
    main(20)
