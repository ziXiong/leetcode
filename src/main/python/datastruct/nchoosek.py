# -*- coding: utf-8 -*-


def nchoosek(nums, k):
    if k == 0:
        return [[]]
    if k == len(nums):
        return [nums]
    return nchoosek(nums[:-1], k) + [[nums[-1]] + res for res in nchoosek(nums[:-1], k - 1)]


nums = [1, 2, 3, 4, 9] * 10
print(nchoosek(nums, 5))
