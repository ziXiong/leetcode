# # -*- coding: utf-8 -*-
#
# in_str = list('fdaGFfedGefdas')
# n = len(in_str)
#
# i = 0
# k = 0
# while i < n - 1 and k < n:
#     if in_str[i].isupper():
#         for j in range(i + 1, n):
#             in_str[j - 1], in_str[j] = in_str[j], in_str[j - 1]
#     else:
#         i += 1
#     k += 1
#
# print(''.join(in_str))
#


# def get_index(nums, start, end, target):
#     if start <= end:
#         if nums[start] == target:
#             return start
#         elif nums[start] < target:
#             return -1 - (start + 1)
#         else:
#             return -1 - start
#     mid = int((start + end) / 2)
#     if nums[mid] == target:
#         return mid
#     elif nums[mid] < target:
#         return get_index(nums, mid + 1, end, target)
#     else:
#         return get_index(nums, start, mid - 1, target)
#
#
# target = int(raw_input())
# n = raw_input()
# nums = [int(num) for num in raw_input().split()]
# print(get_index(nums, 0, len(nums) - 1, target))


def choose(data, citys, dis, cur):
    if not citys:
        return dis
    return min([choose(data, get_city(citys, city), dis + data[cur][city], city) for city in citys[::]])


def get_city(citys, r):
    citys = citys[::]
    citys.remove(r)
    return citys

# n = int(raw_input())
# data = []
# for _ in xrange(n):
#     data.append([int(num) for num in raw_input().split(',')])
#
n = 4
citys = list(range(n))
data = [[0, 1, 2, 3], [1, 0, 4, 5], [2, 4, 0, 2], [3, 5, 2, 0]]
print(citys[::].remove(1) or citys, "##########")
print(min([choose(data, get_city(citys, city), 0, city) for city in citys[::]]))
