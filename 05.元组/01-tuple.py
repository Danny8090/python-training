#!/usr/bin/env python
# coding=utf-8

"""
@author: danny ding
@license: MIT
@contact: goufaner520@outlook.com
@software: Python
@file: 01-tuple.py
@time: 2019/9/1 17:42
@desc: 使用元组

"""


def main():

    # 定义元组
    t = ('骆昊', 38, True, '四川成都')
    print(t)        # ('骆昊', 38, True, '四川成都')

    # 获取元组中的元素
    print(t[0])     # 骆昊
    print(t[3])     # 四川成都

    # 遍历元组中的值
    for member in t:
        print(member, end=' ')      # 骆昊 38 True 四川成都
    print()

    # 重新给元组赋值
    # t[0] = '王大锤'                  # TypeError: 'tuple' object does not support item assignment

    # 变量t重新引用了新的元组原来的元组将被垃圾回收
    t = ('王大锤', 20, True, '云南昆明')
    print(t)                          # ('王大锤', 20, True, '云南昆明')

    # 将元组转换成列表
    person = list(t)
    print(person)                     # ['王大锤', 20, True, '云南昆明']

    # 列表是可以修改它的元素的
    person[0] = '李小龙'
    person[1] = 25
    print(person)                     # ['李小龙', 25, True, '云南昆明']

    # 将列表转换成元组
    fruits_list = ['apple', 'banana', 'orange']
    fruits_tuple = tuple(fruits_list)
    print(fruits_tuple)               # ('apple', 'banana', 'orange')


if __name__ == '__main__':
    main()
