# Write a program to find the node at which the intersection of two singly linked lists begins.
# For example, the following two linked lists:
# A:      a1 → a2
#                    ↘
#                     c1 → c2 → c3
#                    ↗
#    B:  b1 → b2 → b3
# begin to intersect at node c1.
# Notes:
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Knowledge Point:
# * 'a == b' is equal to 'a.__eq__(b)', return value is depend on the __eq__ function.
# * 'a is b' is equal to 'id(a) == id(b)', return value is depend ond

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        pointA = headA
        pointB = headB
        countA, countB = False, False

        if pointA is None or pointB is None:
            return None

        while True:
            if pointA is pointB:
                return pointA
            pointA = pointA.next
            pointB = pointB.next
            if pointA is None:
                if countA is True:
                    return None
                pointA = headB
                countA = True
            if pointB is None:
                if countB is True:
                    return None
                pointB = headA
                countB = True
