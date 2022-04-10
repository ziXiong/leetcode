// Source : https://leetcode.com/problems/add-two-numbers/
// Author : quezixiong
// Date   : 2022-04-10

/***************************************************************************************************** 
 *
 * You are given two non-empty linked lists representing two non-negative integers. The digits are
 * stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and 
 * return the sum as a linked list.
 * 
 * You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 * 
 * Example 1:
 * 
 * Input: l1 = [2,4,3], l2 = [5,6,4]
 * Output: [7,0,8]
 * Explanation: 342 + 465 = 807.
 * 
 * Example 2:
 * 
 * Input: l1 = [0], l2 = [0]
 * Output: [0]
 * 
 * Example 3:
 * 
 * Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
 * Output: [8,9,9,9,0,0,0,1]
 * 
 * Constraints:
 * 
 * 	The number of nodes in each linked list is in the range [1, 100].
 * 	0 <= Node.val <= 9
 * 	It is guaranteed that the list represents a number that does not have leading zeros.
 ******************************************************************************************************/

package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	var head *ListNode
	var lastNode *ListNode
	isCarry := false
	for l1 != nil || l2 != nil {
		var digitSum int
		if l1 != nil {
			digitSum += l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			digitSum += l2.Val
			l2 = l2.Next
		}
		if isCarry {
			digitSum += 1
		}

		curNode := &ListNode{Val: digitSum%10}
		if head == nil {
			head = curNode
		} else {
			lastNode.Next = curNode
		}

		isCarry = digitSum >= 10
		lastNode = curNode
	}

	if isCarry {
		lastNode.Next = &ListNode{Val: 1}
	}

	return head
}