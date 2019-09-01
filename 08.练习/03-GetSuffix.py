#!/usr/bin/env python
# coding=utf-8

"""
@author: danny ding
@license: MIT
@contact: goufaner520@outlook.com
@software: Python
@file: 03-GetSuffix.py
@time: 2019/9/1 21:50
@desc: 设计一个函数返回给定文件名的后缀名。
获取文件名的后缀名
    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
"""


def get_suffix(filename, has_dot=False):
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''


def main():
    # 打印点.
    # print(get_suffix('File_Settings.png', has_dot=True))

    # 不打印点.
    print(get_suffix('无师自通：Photoshop CS5图像处理与典型实例从入门到精通（全彩超值版） PDF 扫描版.pdf'))


if __name__ == '__main__':
    main()
