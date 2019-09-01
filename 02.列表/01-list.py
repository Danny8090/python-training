# coding=utf-8


def main():
    list1 = [1, 3, 5, 7, 10]
    print(list1)        # [1, 3, 5, 7, 10]

    list2 = ['hello'] * 5
    print(list2)        # ['hello', 'hello', 'hello', 'hello', 'hello']

    # 计算列表长度(元素个数)
    print(len(list1))       # 5
    print(len(list2))       # 5

    # 下标(索引)运算
    print(list1[0])         # 1
    print(list1[3])         # 7
    # print(list1[5])         # IndexError: list index out of range
    print(list1[-1])        # 10
    print(list1[-3])        # 5

    list1[2] = 100
    print(list1)            # [1, 3, 100, 7, 10]

    # 添加元素
    list1.append(200)       # append添加在后面
    print(list1)            # [1, 3, 100, 7, 10, 200]
    list1.insert(1, 400)    # insert添加在前面
    print(list1)            # [1, 400, 3, 100, 7, 10, 200]
    list1 += [1000, 2000]   # 添加后面
    print(list1)            # [1, 400, 3, 100, 7, 10, 200, 1000, 2000]

    # 删除元素
    list1.remove(3)
    print(list1)            # [1, 400, 100, 7, 10, 200, 1000, 2000]

    if 1234 in list1:
        list1.remove(1234)

    del list1[0]
    print(list1)            # [400, 100, 7, 10, 200, 1000, 2000]

    # 清空列表元素
    list1.clear()
    print(list1)            # []


if __name__ == '__main__':
    main()
