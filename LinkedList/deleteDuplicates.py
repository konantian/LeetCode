#Source : https://leetcode.com/problems/remove-duplicates-from-sorted-list/
#Author : Yuan Wang
#Date   : 2018-07-25
'''
********************************************************************************** 
*Given a sorted linked list, delete all duplicates such that each element appear only once.
*
*Example 1:
*
*Input: 1->1->2
*Output: 1->2
*Example 2:
*
*Input: 1->1->2->3->3
*Output: 1->2->3
**********************************************************************************/
'''
from SLinkedList import SLinked_List

def deleteDuplicates(head):
	"""
	:type head: ListNode
	:rtype: ListNode
	"""
	current=head
	while current != None and current.next != None:
		if current.val == current.next.val:
			current.next=current.next.next
		else:
			current=current.next
	return head


sll=SLinked_List()

sll.append(1)
sll.append(1)
sll.append(2)
sll.append(2)
sll.append(3)
sll.append(3)
sll.append(3)


print(sll)
deleteDuplicates(sll.head)
print(sll)