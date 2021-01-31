'''
Source : https://leetcode.com/problems/merge-two-sorted-lists/
Author : Yuan Wang
Date   : 2021-01-31

/*************************************************************************************** 
*Merge two sorted linked lists and return it as a sorted list. The list should be made 
*by splicing together the nodes of the first two lists.
*
*Example1 :
*Input: l1 = [1,2,4], l2 = [1,3,4]
*Output: [1,1,2,3,4,4]
****************************************************************************************/
 '''
 
 #Iterative solution, time complexity : O(n), space complexity : O(1)
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = cur = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next