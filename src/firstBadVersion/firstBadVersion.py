# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        beg = 1
        while not beg == n:
            middle = (beg + n) / 2
            if isBadVersion(middle):
                n = middle
            else:
                beg = middle + 1
        return beg


