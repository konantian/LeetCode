#Source : https://leetcode.com/problems/insertion-sort-list/
#Author : Yuan Wang
#Date   : 2021-02-01
'''
********************************************************************************** 
*Sort a linked list using insertion sort.
*
*Example1 :
*Input: 4->2->1->3
*Output: 1->2->3->4
**********************************************************************************/
'''

#time complexity : O(n) space complexity : O(1)
def insertionSortList(self, head: ListNode) -> ListNode:
    p = ListNode(0)
    dummy = p
    dummy.next = head
    current = head
    while current and current.next:
        val = current.next.val
        if current.val < val:
            current = current.next
            continue
        if p.next.val > val:
            p = dummy
        while p.next.val < val:
            p = p.next
        temp = current.next
        current.next = temp.next
        temp.next = p.next
        p.next = temp
    return dummy.next