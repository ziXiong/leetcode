# Given a list of non negative integers, arrange them such that they form the largest number.
# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
# Note: The result may be very large, so you need to return a string instead of an integer.


def get_bit(num, k):
    bitlist = []
    d = 1
    p = 10
    bitlist[0] = num % 10
    while num > p:
        bitlist[d] = (num / p) % 10
        d += 1
        p *= 10
    return bitlist[-k]


class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, nums):
        out = ''
        while len(nums) > 0:
            for num in nums:
                pass


