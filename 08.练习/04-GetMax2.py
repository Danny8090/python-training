#!/usr/bin/env python
# coding=utf-8

"""
@author: danny ding
@license: MIT
@contact: goufaner520@outlook.com
@software: Python
@file: 04-GetMax2.py
@time: 2019/9/1 22:04
@desc: 设计一个函数返回传入的列表中最大和第二大的元素的值。

"""


def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2


if __name__ == '__main__':
    list1 = [0, 111, 2, 3, 4, 50, 6, 7, 8, 9, 10]
    print(max2(list1))
