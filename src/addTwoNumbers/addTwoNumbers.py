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
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        flag = 0
        cursor1 = l1
        cursor2 = l2
        while True:
            cursor1 = cursor1.next
            if cursor1 is None:
                flag += 1
                cursor1 = l2
                if flag == 2:
                    cursor2 = cursor2.next
                    while cursor1 is not None:
                        cursor2.val += cursor1.val
                        cursor1 = cursor1.next
                        cursor2 = cursor2.next
                    return l1
            cursor2 = cursor2.next
            if cursor2 is None:
                flag += 1
                cursor2 = l1
                if flag == 2:
                    while cursor1 is not None:
                        cursor1.val += cursor2.val
                        cursor1 = cursor1.next
                        cursor2 = cursor2.next
                    return l2

        