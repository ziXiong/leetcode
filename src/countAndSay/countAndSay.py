"""
Count And Say
created: 2014/10/25
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
"""

# Knowledge Point:
# * usage of groupby
# * iterator to list

from itertools import groupby


class Solution:
    # @return a string
    def countAndSay(self, n):
        say = '1'
        for _ in range(n-1):
            next = ''
            for group in [list(g) for k, g in groupby(say, lambda x: x)]:
                next += str(len(group)) + group[0]
            say = next
        return say
