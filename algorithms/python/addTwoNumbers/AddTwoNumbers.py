# You are given two linked lists representing two non-negative numbers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Remember:
# Readability is also important, Don't sacrifice it for insignificant algorithm complicity.
class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        sum = 0
        result = curnode = ListNode(0)
        while l1 is not None or l2 is not None:
            sum /= 10
            if l1 is not None:
                sum += l1.val
                l1 = l1.next
            if l2 is not None:
                sum += l2.val
                l2 = l2.next
            curnode.next = ListNode(sum % 10)
            curnode = curnode.next
        if sum / 10:
            curnode.next = ListNode(sum / 10)
        return result.next

