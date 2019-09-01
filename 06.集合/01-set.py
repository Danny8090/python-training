#!/usr/bin/env python
# coding=utf-8

"""
@author: danny ding
@license: MIT
@contact: goufaner520@outlook.com
@software: Python
@file: 01-set.py
@time: 2019/9/1 17:51
@desc: 使用集合

"""

'''
集合：Python中的集合跟数学上的集合是一致的，不允许有重复元素，而且可以进行交集、并集、差集等运算。
集合a和b交集(a & b)：a.intersection(b)
集合a和b并集(a | b)：a.union(b)
集合a和b差集(a - b)：a.difference(b)
集合a和b对称差(a ^ b)：a.symmetric_difference(b)
'''


def main():
    set1 = {1, 2, 3, 3, 3, 2}
    # 集合中重复元素被忽略
    print(set1)                             # {1, 2, 3}
    print('Length =', len(set1))            # Length = 3

    set2 = set(range(1, 10))
    print(set2)                             # {1, 2, 3, 4, 5, 6, 7, 8, 9
    # 给集合添加已有元素，不会出现
    set1.add(4)
    print(set1)                             # {1, 2, 3, 4}
    # 给集合添加新元素
    set1.add(5)
    print(set1)                             # {1, 2, 3, 4, 5}
    # 给集合添加多个元素
    set2.update([11, 12])
    print(set2)                             # {1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12}
    # 删除集合中的指定元素
    set2.discard(5)
    print(set2)                             # {1, 2, 3, 4, 6, 7, 8, 9, 11, 12}

    # remove的元素如果不存在会引发KeyError
    if 4 in set2:
        set2.remove(4)
    print(set2)                             # {1, 2, 3, 6, 7, 8, 9, 11, 12}

    # 遍历集合容器
    for elem in set2:
        print(elem ** 2, end=' ')           # 1 4 9 36 49 64 81 121 144
    print()

    # 将元组转换成集合
    tuple1 = (1, 2, 3, 3, 2, 1)
    set3 = set(tuple1)
    print(set3.pop())                       # 1
    print(set3)                             # {2, 3}

    # 集合的交集、并集、差集、对称差运算
    print(set1)                             # {1, 2, 3, 4, 5}
    print(set2)                             # {1, 2, 3, 6, 7, 8, 9, 11, 12}
    # 交集
    print(set1 & set2)                      # {1, 2, 3}
    print(set1.intersection(set2))          # {1, 2, 3}
    # 并集
    print(set1 | set2)                      # {1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12}
    print(set1.union(set2))                 # {1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12}
    # 差集
    print(set1 - set2)                      # {4, 5}
    print(set1.difference(set2))            # {4, 5}
    print(set2 - set1)                      # {6, 7, 8, 9, 11, 12}
    # 对称差运算
    print(set1 ^ set2)                      # {4, 5, 6, 7, 8, 9, 11, 12}
    print(set1.symmetric_difference(set2))  # {4, 5, 6, 7, 8, 9, 11, 12}

    # 判断子集和超集
    print(set1)                             # {1, 2, 3, 4, 5}
    print(set2)                             # {1, 2, 3, 6, 7, 8, 9, 11, 12}
    print(set3)                             # {2, 3}
    print(set2 <= set1)                     # False
    print(set2.issubset(set1))              # False

    print(set3 <= set1)                     # True
    print(set3.issubset(set1))              # True

    print(set1 >= set2)                     # False
    print(set1.issuperset(set2))            # False

    print(set1 >= set3)                     # True
    print(set1.issuperset(set3))            # True


if __name__ == '__main__':
    main()