#Source : https://leetcode.com/problems/linked-list-components/
#Author : Yuan Wang
#Date   : 2021-01-13
'''
********************************************************************************** 
*We are given head, the head node of a linked list containing unique integer values.
*
*We are also given the list G, a subset of the values in the linked list.
*
*Return the number of connected components in G, where two values are connected 
*if they appear consecutively in the linked list.
*
*Example 1:
*
*Input: head: 0->1->2->3
*G = [0, 1, 3]
*Output: 2
*Example 2:
*
*Input: head: 0->1->2->3->4
*Output: 2
**********************************************************************************/
'''
from SLinkedList import SLinked_List, ListNode
from typing import List

def numComponents(head: ListNode, G: List[int]) -> int:
    connected = 0
    current = head
    G = set(G)
    connect = False
    while current:
        if current.val in G:
            if not connect:
                connect = True
                connected += 1
        else:
            if connect:
                connect = False
            
        current = current.next
        
    return connected


elements=[0,1,2,3,4]
G = [0,3,1,4]

sll=SLinked_List()
sll.add_elements(elements)
print(sll)
print(numComponents(sll.head, G))