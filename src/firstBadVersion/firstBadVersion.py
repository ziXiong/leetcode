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
        return self.findBadVersion(1, n)

    def findBadVersion(self, start, end):
        middle = (start + end) / 2
        if start == end:
            return start
        elif isBadVersion(middle):
            return self.findBadVersion(start, middle)
        else:
            return self.findBadVersion(middle+1, end)

