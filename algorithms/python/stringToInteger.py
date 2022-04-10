# Implement atoi to convert a string to an integer.
# Hint: Carefully consider all possible input cases.
# If you want a challenge, please do not see below and ask yourself what are the possible input cases.
# Notes: It is intended for this problem to be specified vaguely (ie, no given input specs).
# You are responsible to gather all the input requirements up front.
# Requirements for atoi:
# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.
# Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible,
#  and interprets them as a numerical value.
# The string can contain additional characters after those that form the integral number,
#  which are ignored and have no effect on the behavior of this function.
# If the first sequence of non-whitespace characters in str is not a valid integral number,
# or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
# If no valid conversion could be performed, a zero value is returned.
# If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.


# Remember:
# String in python could not be changed(like a tuple), just change and copy.
class Solution:
    # @return an integer
    def atoi(self, str):
        str = str.strip()
        sign = 1
        if str and str[0] in ['-', '+']:
            if str[0] == '-':
                sign = -1
            str = str[1:]
        n = len(str)
        ret = 0
        for i in range(n):
            key = str[i]
            if key.isdigit():
                ret = ret * 10 + int(key)
            else:
                return sign * ret
        return sign * ret
