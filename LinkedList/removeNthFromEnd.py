#Source : https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
#Author : Yuan Wang
#Date   : 2018-07-25
'''
********************************************************************************** 
*Given a linked list, remove the n-th node from the end of list and return its head.
*
*Example:
*
*Given linked list: 1->2->3->4->5, and n = 2.
*
*After removing the second node from the end, the linked list becomes 1->2->3->5.
*Note:
*
*Given n will always be valid.
*
*Follow up:
*
*Could you do this in one pass?
**********************************************************************************/
'''
from SLinkedList import SLinked_List

def removeNthFromEnd(head,n):
	temp=head
	lead=head
	for i in range(n):
		lead=lead.next
	if lead == None:
		head=head.next
		return head
	while lead.next != None:
		lead=lead.next
		head=head.next
	head.next=head.next.next
	head=temp

	return head
	
sll=SLinked_List()

sll.append(1)
sll.append(2)
sll.append(3)
sll.append(4)
sll.append(5)

print(sll)
removeNthFromEnd(sll.head,2)
print(sll)
