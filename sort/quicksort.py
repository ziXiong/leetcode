# -*- coding: utf-8 -*-
"""
快排, 原地排序, 两边同时进行
要点: 每个外层循环还可以来内层的循环; 递归逻辑的零界点
改进项: 随机去哨兵; 三个哨兵选中间值
"""


def quick_sort(in_list, left, right):
    if left < right:
        pivot = in_list[right]
        m, n = left, right - 1
        while m < n:
            while in_list[m] <= pivot and m < n:
                m += 1
            while in_list[n] >= pivot and m < n:
                n -= 1
            in_list[m], in_list[n] = in_list[n], in_list[m]

        if in_list[m] < pivot:
            m += 1
        in_list[m], in_list[right] = pivot, in_list[m]
        quick_sort(in_list, left, m - 1)
        quick_sort(in_list, m + 1, right)


in_list = [3, 1, 3, 4, 5, 143543,6, 8, 4, 8, 9, 4, 1, 1000000]
quick_sort(in_list, 0, len(in_list) - 1)
print(in_list)

