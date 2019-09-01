#!/usr/bin/env python
# coding=utf-8

"""
@author: danny ding
@license: MIT
@contact: goufaner520@outlook.com
@software: Python
@file: 01-dict.py
@time: 2019/9/1 18:30
@desc: 使用字典

"""

'''
字典是另一种可变容器模型，类似于我们生活中使用的字典，它可以存储任意类型对象，
与列表、集合不同的是，字典的每个元素都是由一个键和一个值组成的“键值对”，键和值通过冒号分开。
'''


def main():
    scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}

    # 通过键可以获取字典中对应的值
    print(scores['骆昊'])                         # 95
    print(scores['狄仁杰'])                       # 82

    # 对字典进行遍历(遍历的其实是键再通过键取对应的值)
    for elem in scores:
        # 骆昊	--->	95  白元芳	--->	78  狄仁杰	--->	82
        print('%s\t--->\t%d' % (elem, scores[elem]))

    # 更新字典中的元素
    scores['白元芳'] = 65
    scores['诸葛王朗'] = 71
    scores.update(冷面=67, 方启鹤=85)
    # {'骆昊': 95, '白元芳': 65, '狄仁杰': 82, '诸葛王朗': 71, '冷面': 67, '方启鹤': 85}
    print(scores)

    if '武则天' in scores:
        print(scores['武则天'])
    print(scores.get('武则天'))                # None

    # get方法也是通过键获取对应的值但是可以设置默认值
    print(scores.get('武则天', 60))            # 60

    # 删除字典中的元素
    # {'骆昊': 95, '白元芳': 65, '狄仁杰': 82, '诸葛王朗': 71, '冷面': 67, '方启鹤': 85}
    print(scores)
    print(scores.popitem())                     # ('方启鹤', 85)
    print(scores.popitem())                     # ('冷面', 67)
    print(scores.pop('骆昊', 100))               # 95
    # {'白元芳': 65, '狄仁杰': 82, '诸葛王朗': 71}
    print(scores)

    # 清空字典
    scores.clear()
    print(scores)                               # {}


if __name__ == '__main__':
    main()
