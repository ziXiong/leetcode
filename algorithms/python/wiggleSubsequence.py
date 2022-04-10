# -*- coding: utf-8 -*-


class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        last = 1
        status = None

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            elif status is None:
                last = 2
                status = True if nums[i] > nums[i - 1] else False
            elif status is True:
                if nums[i] < nums[i - 1]:
                    last += 1
                    status = False
            elif status is False:
                if nums[i] > nums[i - 1]:
                    last += 1
                    status = True

        return last
