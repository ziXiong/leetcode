# -*- coding: utf-8 -*-


class Solution(object):
    def subsets(self, nums):

        n = len(nums)
        sets = []

        for i in range(2 ** n):
            this_set = []
            for j in range(n):
                if (i >> j) & 1:
                    this_set.append(nums[j])
                    print(i, nums[j])
            sets.append(this_set)

        return sets

nums = [1, 2, 3]

print(subsets(nums))



