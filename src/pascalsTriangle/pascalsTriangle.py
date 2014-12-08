# Given numRows, generate the first numRows of Pascal's triangle.
# For example, given numRows = 5,
# Return
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]


class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0:
            return []
        ret = [[1]]
        for n in range(1, numRows):
            tmp_ret = [1]
            for i in range(1, n):
                tmp_ret.append(ret[n-1][i-1] + ret[n-1][i])
            tmp_ret.append(1)
            ret.append(tmp_ret)
        return ret
