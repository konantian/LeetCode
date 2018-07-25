#Source : https://leetcode.com/problems/palindrome-linked-list/
#Author : Yuan Wang
#Date   : 2018-07-25
'''
********************************************************************************** 
*Given a singly linked list, determine if it is a palindrome.
*
*Example 1:
*
*Input: 1->2
*Output: false
*Example 2:
*
*Input: 1->2->2->1
*Output: true
**********************************************************************************/
'''
from SLinkedList import SLinked_List

#Self solution, Time complexity:O(n) Space complexity:O(n)
def isPalindromeA(head):
	"""
	:type head: ListNode
	:rtype: bool
	"""
	result=[]
	current=head
	while(current != None):
		result.append(current.val)
		current=current.next
	
	return result==result[::-1]

#Other solution, Time complexity:O(n) Space complexity:O(1)
def isPalindromeB(head):
	"""
	:type head: ListNode
	:rtype: bool
	"""
	slow = fast = head
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
	node = None
	while slow:
		nxt = slow.next
		slow.next = node
		node = slow
		slow = nxt
	
	while node and head:
		if node.val != head.val:
			return False
		node = node.next
		head = head.next
	return True

elements=[1,2,3,4,3,2,1]

sll=SLinked_List()
sll.add_elements(elements)
print(sll)
print(isPalindromeB(sll.head))