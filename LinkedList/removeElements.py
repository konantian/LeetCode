#Source : https://leetcode.com/problems/remove-linked-list-elements/
#Author : Yuan Wang
#Date   : 2018-07-25
'''
********************************************************************************** 
*Remove all elements from a linked list of integers that have value val.
*
*Example:
*
*Input:  1->2->6->3->4->5->6, val = 6
*Output: 1->2->3->4->5
**********************************************************************************/
'''
from SLinkedList import SLinked_List

def removeElements(head, val):
	"""
	:type head: ListNode
	:type val: int
	:rtype: ListNode
	"""
	current=head
	previous=None
	while current != None:
		if current.val == val:
			if previous == None:
				head=current.next
			else:
				previous.next=current.next
				current=current.next
		else:
			previous=current
			current=current.next
	
	return head

elements=[1,2,6,3,4,5,6]

sll=SLinked_List()
sll.add_elements(elements)

print(sll)
removeElements(sll.head,6)
print(sll)