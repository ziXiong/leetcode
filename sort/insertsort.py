# -*- coding: utf-8 -*-

"""
插入排序
要点: 每个变量, 在纸上研究好他们的意义; 存储为tmp而不是每次交换, 会减少复制数
复杂度: 总共选择n/2次, 每次选择都遍历n-i次, 时间复杂度为n**2。
改进: 插入过程改为二分查找
"""


def insert_sort(in_list):
    for i in range(len(in_list)):
        tmp = in_list[i]
        while i > 0 and tmp < in_list[i - 1]:
            in_list[i] = in_list[i - 1]
            i -= 1
        in_list[i] = tmp


l = [3, 4, 7, 4, 8, 0, 5, 4, 8, 10, 1, 2342]
insert_sort(l)

print(l)
