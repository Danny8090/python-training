#!/usr/bin/env python
# coding=utf-8

"""
@author: danny ding
@license: (C) Copyright 2013-2019, Node Supply Chain Manager Corporation Limited.
@contact: goufaner520@outlook.com
@software: Python
@file: ${NAME}.py
@time: ${DATE} ${TIME}
@desc:03-对列表的排序操作

"""


def main():
    list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    list2 = sorted(list1)
    # sorted函数返回列表排序后的拷贝不会修改传入的列表
    # 函数的设计就应该像sorted函数一样尽可能不产生副作用
    print(list1)  # ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    print(list2)  # ['apple', 'blueberry', 'internationalization', 'orange', 'zoo']

    list3 = sorted(list1, reverse=True)
    print(list1)  # ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    print(list3)  # ['zoo', 'orange', 'internationalization', 'blueberry', 'apple']

    # 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
    list4 = sorted(list1, key=len)
    print(list1)  # ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    print(list4)  # ['zoo', 'apple', 'orange', 'blueberry', 'internationalization']

    # 给列表对象发出排序消息直接在列表对象上进行排序
    list1.sort(reverse=True)
    print(list1)  # ['zoo', 'orange', 'internationalization', 'blueberry', 'apple']


if __name__ == '__main__':
    main()
