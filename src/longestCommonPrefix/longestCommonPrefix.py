# Write a function to find the longest common prefix string amongst an array of st


class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        lcp = ''
        for n in range(len(strs[0])):
            key = strs[0][n]
            for s in strs:
                if len(s) < n+1 or s[n] != key:
                    return lcp
            lcp += key
        return lcp