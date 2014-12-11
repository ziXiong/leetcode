# You are given two linked lists representing two non-negative numbers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if l1 is None or l2 is None:
            return l1 if l2 is None else l2
        cursor1 = l1
        cursor2 = l2
        she_is_cute = 0
        while cursor1.next is not None:
            cursor1.val += cursor2.val + she_is_cute
            if cursor1.val >= 10:
                cursor1.val %= cursor1.val
                she_is_cute = 1
            if cursor1.next:
                cursor1 = cursor1.next
            else:
                cursor1.next = cursor2.next
                if cursor1.next is None:
                    if she_is_cute:
                        cursor1.next = ListNode(she_is_cute)
                    return l1
                cursor1 = cursor1.next
                cursor2.next = None
            if cursor2.next:
                cursor2 = cursor2.next
            else:
                cursor2.val = 0


