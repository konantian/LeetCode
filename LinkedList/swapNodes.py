#Source : https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
#Author : Yuan Wang
#Date   : 2021-01-13
'''
********************************************************************************** 
*You are given the head of a linked list, and an integer k.

*Return the head of the linked list after swapping the values of the kth node 
*from the beginning and the kth node from the end (the list is 1-indexed).
*
*Example:
*
*Input: head = [1,2,3,4,5], k = 2
*Output: [1,4,3,2,5]
*
*Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
*Output: [7,9,6,6,8,7,3,0,9,5]
**********************************************************************************/
'''
from SLinkedList import SLinked_List

def swapNodes(head, k: int):
    if not head.next: return head
    
    left, right = None, head
    tail = head
    for _ in range(k):
        left = tail
        tail = tail.next
    
    while tail:
        right = right.next
        tail = tail.next
    left.val, right.val = right.val,left.val
    return head


elements=[1,2,3,4,5]
k = 2

sll=SLinked_List()
sll.add_elements(elements)

print(sll)
swapNodes(sll.head, k)
print(sll)