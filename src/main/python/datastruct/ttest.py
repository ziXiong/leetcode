# -*- coding: utf-8 -*-



def get_max(nums, n, allow_0):
    if n < 0 or (n == 0 and not allow_0):
        return 0
    return max(nums[n] + get_max(nums, n - 2), get_max(nums, n - 1, allow_0))


# times = int(raw_input())
# for _ in xrange(times):
#     nums = [int(num) for num in raw_input().split(',')]
#     n = len(nums) - 1
#     print(max(get_max(nums, n - 2, False) + nums[n], get_max(nums, n - 1, True)))


import sys

print(sys.stdin.readline())





