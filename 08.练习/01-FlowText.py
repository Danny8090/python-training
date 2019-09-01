#!/usr/bin/env python
# coding=utf-8

"""
@author: danny ding
@license: MIT
@contact: goufaner520@outlook.com
@software: Python
@file: 01-在屏幕上显示跑马灯文字.py
@time: 2019/9/1 18:51
@desc: 在屏幕上显示跑马灯文字

"""

import os
import time


def main():
    content = '北京欢迎你为你开天辟地…………'
    # 解释：
    # print(content[1:])
    # print(content[0])
    # content = content[1:] + content[0]
    # print(content)
    # content = content[1:] + content[0]
    # print(content)
    # content = content[1:] + content[0]
    # print(content)

    while True:
        # 清理屏幕上的输出,请在cmd窗口运行
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()
