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
from SLinkedList import SLinked_List

def reverseList(head):
	"""
	:type head: ListNode
	:rtype: ListNode
	"""
	currentNode=head
	if head != None:
		nextNode = head.next
		currentNode.next = None

		while nextNode != None:
			aux = nextNode.next
			nextNode.next = currentNode
			currentNode = nextNode
			nextNode = aux
	
	return currentNode

sll=SLinked_List()

sll.append(1)
sll.append(2)
sll.append(3)
sll.append(4)
sll.append(5)


print(sll)
reverseList(sll.head)
print(sll)