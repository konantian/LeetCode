#Source : https://leetcode.com/problems/reverse-linked-list/
#Author : Yuan Wang
#Date   : 2018-07-25
'''
********************************************************************************** 
*Reverse a singly linked list.
*
*Example:
*
*Input: 1->2->3->4->5->NULL
*Output: 5->4->3->2->1->NULL
*Follow up:
*
*A linked list can be reversed either iteratively or recursively. Could you implement both?
**********************************************************************************/
'''
from SLinkedList import SLinked_List, ListNode

def reverseList(head: ListNode) -> ListNode:
	current = head
	previous = None
	while current:
		temp = current.next
		current.next = previous
		previous = current
		current = temp
	return previous

elements=[1,2,3,4,5]

sll=SLinked_List()
sll.add_elements(elements)

print(sll)
reverseList(sll.head)
print(sll)
