#!/usr/bin/env python
# coding=utf-8

"""
@author: danny ding
@license: MIT
@contact: goufaner520@outlook.com
@software: Python
@file: 02-VerificationCode.py
@time: 2019/9/1 19:23
@desc: 设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
生成指定长度的验证码
:param code_len: 验证码的长度(默认4个字符)
:return: 由大小写英文字母和数字构成的随机验证码
"""

import random


def generate_code(code_len=4):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1

    # print(len(all_chars))
    # print(last_pos)

    # for i in range(10):
    #     print(i)

    code = ''

    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
        # print(code)
    return code


if __name__ == '__main__':
    print(generate_code())

