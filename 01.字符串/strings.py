# coding=utf-8

def main():
    str1 = 'hello world'

    # len函数计算字符串长度
    print(len(str1))    # 11

    # capitalize函数字符串首字母大写
    print(str1.capitalize())    # Hello world

    # upper函数字符串变大写
    print(str1.upper())    # HELLO WORLD

    # find函数从字符串中查找子串所在位置
    print(str1.find('or'))    # 7
    print(str1.find('shit'))    # -1

    # index函数与find函数类似但找不到子串时会引发异常
    print(str1.index('or'))     # 7
    # print(str1.index('shit'))       # ValueError: substring not found

    # startswith函数检查字符串是否以指定的字符串开头
    print(str1.startswith('He'))        # False
    print(str1.startswith('hel'))       # True

    # endswith函数检查字符串是否以指定的字符串结尾
    print(str1.endswith('!'))       # False
    print(str1.endswith('ld'))      # True

    # center函数将字符串以指定的宽度居中并在两侧填充指定的字符
    print(str1.center(50, '*'))     # *******************hello world*******************

    # rjust函数将字符串以指定的宽度靠右放置左侧填充指定的字符
    print(str1.rjust(50, '_'))      # _______________________________________hello world



    str2 = 'abc12345'

    # 从字符串中取出指定位置的字符(下标运算)([0][1][2]...[n])
    print(str2[2])      # c
    # 字符串切片(从指定的开始索引到指定的结束索引)
    '''
    切片：切片操作要提供三个参数 [start_index:  stop_index:  step]
    start_index是切片的起始位置。
    stop_index是切片的结束位置（不包括）
    step可以省略，默认值是1，步长值不能为0，不然会报错ValueError
    
    当 step 是正数时，以list[start_index]元素位置开始， step做为步长到list[stop_index]元素位置（不包括）为止，从左向右截取，
    start_index和stop_index不论是正数还是负数索引还是混用都可以，但是要保证 list[stop_index]元素的【逻辑】位置必须在list[start_index]元素的【逻辑】位置右边，否则取不出元素
    
    当 step 是负数时，以list[start_index]元素位置开始， step做为步长到list[stop_index]元素位置（不包括）为止，从右向左截取
    start_index和stop_index不论是正数还是负数索引还是混用都可以，但是要保证 list[stop_index]元素的【逻辑】位置必须在list[start_index]元素的【逻辑】位置左边，否则取不出元素
    
    '''
    print(str2[2:5])        # c12
    print(str2[2:])         # c12345
    print(str2[2::2])       # c24
    print(str2[::2])        # ac24
    print(str2[::-1])       # 54321cba 倒序
    print(str2[::1])        # abc12345 复制（不这样写）
    print(str2[:])          # abc12345 复制
    print(str2[-3:-1])      # 34



    # isdigit函数检查字符串是否由数字构成
    print(str2.isdigit())       # False

    # isalpha函数检查字符串是否以字母构成
    print(str2.isalpha())       # False

    # isalnum函数检查字符串是否以数字和字母构成
    print(str2.isalnum())       # True



    str3 = '  jackfrued@126.com '

    print(str3)     # '  jackfrued@126.com '

    # strip获得字符串修剪左右两侧空格的拷贝
    print(str3.strip())     # jackfrued@126.com




    # 列表操作
    alist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 取前一部分
    print(alist[:5])        # [0, 1, 2, 3, 4]

    # 取后一部分
    print(alist[-5:])       # [5, 6, 7, 8, 9]

    # 取偶数位置元素
    print(alist[::2])       # [0, 2, 4, 6, 8]

    # 取奇数位置元素
    print(alist[1::2])      # [1, 3, 5, 7, 9]

    # 浅复制，等价于list.copy()更加面向对象的写法
    print(alist[:])         # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 返回一个逆序列表，推荐reversed(list)的写法，更直观易懂
    print(alist[::-1])      # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(list(reversed(alist)))        # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

    # 在某个位置插入多个元素
    alist[3:3] = ['a', 'b', 'c']
    print(alist)            # [0, 1, 2, 'a', 'b', 'c', 3, 4, 5, 6, 7, 8, 9]

    # 在开始位置之前插入多个元素
    alist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    alist[:0] = ['a', 'b', 'c']
    print(alist)            # ['a', 'b', 'c', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 替换多个元素
    alist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    alist[0:3] = ['a', 'b', 'c']
    print(alist)            # ['a', 'b', 'c', 3, 4, 5, 6, 7, 8, 9]

    # 删除切片
    alist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    del alist[3:6]
    print(alist)            # [0, 1, 2, 6, 7, 8, 9]










if __name__ == '__main__':
    main()
