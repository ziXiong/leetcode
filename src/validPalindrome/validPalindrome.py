# valid Palindrome
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
#
# Note:
# Have you consider that the string might be empty? This is a good question to ask during an interview.
#
# For the purpose of this problem, we define empty string as valid palindrome.


class Solution:

    def isPalindrome(self, s):

        n = len(s)
        pointA = 0
        pointB = n - 1

        while pointA < pointB:
            while not s[pointA].isalnum() and pointA < pointB:
                pointA += 1
            while not s[pointB].isalnum() and pointA < pointB:
                pointB -= 1
            if s[pointA].lower() != s[pointB].lower():
                return False
            pointA += 1
            pointB -= 1
        return True

