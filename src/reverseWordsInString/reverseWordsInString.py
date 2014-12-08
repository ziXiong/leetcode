__author__ = 'harley'
# Given an input string, reverse the string word by word.

# For example,
# Given s = "the sky is blue",
# return "blue is sky the".

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        words = s.split()
        return ' '.join(words[::-1])
