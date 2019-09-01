#!/usr/bin/env python
# coding=utf-8

"""
@author: danny ding
@license: (C) Copyright 2013-2019
@contact: goufaner520@outlook.com
@software: Python
@file: 04-使用列表的生成式语法来创建列表.py
@time: 2019/9/1 0:39
@desc:使用列表的生成式语法来创建列表

"""

import sys


def main():
    f = [x for x in range(1, 10)]
    print(f)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 用列表的生成表达式语法创建列表容器
    # 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间

    f = [x ** 2 for x in range(1, 1000)]
    print(sys.getsizeof(f))  # 查看对象占用内存的字节数
    print(f)

    # 请注意下面的代码创建的不是一个列表而是一个生成器对象
    # 通过生成器可以获取到数据但它不占用额外的空间存储数据
    # 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间

    f = (x ** 2 for x in range(1, 1000))
    print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间
    print(f)  # <generator object main.<locals>.<genexpr> at 0x0000026C1C650F48>
    print(type(f))  # <class 'generator'>
    for val in f:
        print(val)


if __name__ == '__main__':
    main()
