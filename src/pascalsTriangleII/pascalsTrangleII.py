# Given an index k, return the kth row of the Pascal's triangle.
# For example, given k = 3,
# Return [1,3,3,1].
# Note:
# Could you optimize your algorithm to use only O(k) extra space?


class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        for i in range(rowIndex+1):
            currow = [1] * (i + 1)
            for j in range(1, i):
                currow[j] = lastrow[j-1] + lastrow[j]
            lastrow = currow
        return currow
