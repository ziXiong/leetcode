#-*- coding: utf-8 -*-
# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
# Note:
# Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
# The solution set must not contain duplicate triplets.
#     For example, given array S = {-1 0 1 2 -1 -4},
#     A solution set is:
#     (-1, 0, 1)
#     (-1, -1, 2)


class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        if len(num) < 3:
            return []
        num.sort()
        silo = {}
        for idx, n in enumerate(num):
            silo[idx] = n
        target = 3 * [1] + (len(num) - 3) * [0]
        idx = [0, 1, 2]
        result = []
        while True:
            r = [silo[idx[0]], silo[idx[1]], silo[idx[2]]]
            if r[0] + r[1] + r[2] == 0 and r not in result:
                result.append(r)
            if idx[0] == len(num) - 3:
                return result
            num_of_zero = 0
            cur_idx = -1
            last_value = target[0]
            for n, cur_value in enumerate(target):
                if cur_value == 1:
                    last_value = 1
                    cur_idx += 1
                if cur_value == 0:
                    if last_value == 0:
                        num_of_zero += 1
                    else:
                        target[n-1], target[n] = 0, 1
                        idx[cur_idx] += 1
                        if num_of_zero:
                            for i in range(cur_idx):
                                target[idx[i]] = 0
                                idx[i] -= num_of_zero
                                target[idx[i]] = 1
                        break


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-2,0,1,1,2]))



