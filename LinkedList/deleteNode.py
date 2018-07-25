#Source : https://leetcode.com/problems/delete-node-in-a-linked-list/
#Author : Yuan Wang
#Date   : 2018-07-25
'''
********************************************************************************** 
*Write a function to delete a node (except the tail) in a singly linked list, 
*given only access to that node.
*
*Given linked list -- head = [4,5,1,9], which looks like following:
*
*   4 -> 5 -> 1 -> 9
*Example 1:
*
*Input: head = [4,5,1,9], node = 5
*Output: [4,1,9]
*Explanation: You are given the second node with value 5, the linked list
*	 should become 4 -> 1 -> 9 after calling your function.
*Example 2:
*
*Input: head = [4,5,1,9], node = 1
*Output: [4,5,9]
*Explanation: You are given the third node with value 1, the linked list
*	 should become 4 -> 5 -> 9 after calling your function.
**********************************************************************************/
'''
from SLinkedList import SLinked_List

def deleteNode(node):
	"""
	:type node: ListNode
	:rtype: void Do not return anything, modify node in-place instead.
	"""
	node.val=node.next.val
	node.next=node.next.next

elements=[1,2,3,4,5]

sll=SLinked_List()
sll.add_elements(elements)

print(sll)
deleteNode(sll.search(4))
print(sll)