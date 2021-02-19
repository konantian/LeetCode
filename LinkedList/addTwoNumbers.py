#Source : https://leetcode.com/problems/add-two-numbers/
#Author : Yuan Wang
#Date   : 2021-02-19
'''
********************************************************************************** 
*You are given two non-empty linked lists representing two non-negative integers. 
*The digits are stored in reverse order, and each of their nodes contains a single 
*digit. Add the two numbers and return the sum as a linked list.
* Example 1
*Input: l1 = [2,4,3], l2 = [5,6,4]
*Output: [7,0,8]
*Explanation: 342 + 465 = 807.
******
'''

def addTwoNumbers(self, l1, l2):
    carry = 0
    root = n = ListNode(0)
    while l1 or l2 or carry:
        v1 = v2 = 0
        if l1:
            v1 = l1.val
            l1 = l1.next
        if l2:
            v2 = l2.val
            l2 = l2.next
        carry, val = divmod(v1+v2+carry, 10)
        n.next = ListNode(val)
        n = n.next
    return root.next