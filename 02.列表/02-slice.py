# coding=utf-8

"""
切片slice
切片：切片操作要提供三个参数 [start_index:  stop_index:  step]
    start_index是切片的起始位置。
    stop_index是切片的结束位置（不包括）
    step可以省略，默认值是1，步长值不能为0，不然会报错ValueError

    当 step 是正数时，以list[start_index]元素位置开始， step做为步长到list[stop_index]元素位置（不包括）为止，从左向右截取，
    start_index和stop_index不论是正数还是负数索引还是混用都可以，但是要保证 list[stop_index]元素的【逻辑】位置必须在list[start_index]元素的【逻辑】位置右边，否则取不出元素

    当 step 是负数时，以list[start_index]元素位置开始， step做为步长到list[stop_index]元素位置（不包括）为止，从右向左截取
    start_index和stop_index不论是正数还是负数索引还是混用都可以，但是要保证 list[stop_index]元素的【逻辑】位置必须在list[start_index]元素的【逻辑】位置左边，否则取不出元素
"""

def main():
    fruits = ['01grape', '02apple', '03strawberry', '04waxberry']
    print(fruits)  # ['01grape', '02apple', '03strawberry', '04waxberry']
    fruits += ['05pitaya', '06pear', '07mango']
    print(fruits)  # ['01grape', '02apple', '03strawberry', '04waxberry', '05pitaya', '06pear', '07mango']

    # 循环遍历列表元素
    for fruit in fruits:
        print(fruit.title(), end=' ')  # 01Grape 02Apple 03Strawberry 04Waxberry 05Pitaya 06Pear 07Mango
    print()

    # 列表切片
    fruits2 = fruits[1:4]
    print(fruits2)  # ['02apple', '03strawberry', '04waxberry']

    fruit3 = fruits  # 没有复制列表只创建了新的引用
    print(fruit3)  # ['01grape', '02apple', '03strawberry', '04waxberry', '05pitaya', '06pear', '07mango']

    # 可以通过完整切片操作来复制列表
    fruits3 = fruits[:]
    print(fruits3)  # ['01grape', '02apple', '03strawberry', '04waxberry', '05pitaya', '06pear', '07mango']

    fruits4 = fruits[-3:-1]
    print(fruits4)  # ['05pitaya', '06pear']

    # 可以通过反向切片操作来获得倒转后的列表的拷贝
    fruits5 = fruits[::-1]
    print(fruits5)  # ['07mango', '06pear', '05pitaya', '04waxberry', '03strawberry', '02apple', '01grape']

if __name__ == '__main__':
    main()
