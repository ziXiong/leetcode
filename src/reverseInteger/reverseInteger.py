#Reverse digits of an integer.

#Example1: x = 123, return 321
#Example2: x = -123, return -321
"""
Have you thought about this?
Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

Throw an exception? Good, but what if throwing an exception is not an option? You would then have to re-design the function (ie, add an extra parameter).
"""

# TODO: solve the overflow problem.
from math import fabs

class Solution:
    # @return an integer
    def reverse(self, x):
        x_str = str(int(fabs(x)))
        reverse = x_str[::-1]
        x_int = int(reverse)
        if x < 0:
            x_int =  -x_int
        return x_int


if __name__ == '__main__':
    solution = Solution()
    input_str = input("the integer to be reversed:")
    input_int = int(input_str)
    output = solution.reverse(input_int)
    print(output)
