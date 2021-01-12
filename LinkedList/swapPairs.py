#Source : https://leetcode.com/problems/swap-nodes-in-pairs/
#Author : Yuan Wang
#Date   : 2021-01-12
'''
********************************************************************************** 
*Given a linked list, swap every two adjacent nodes and return its head.
*
*Example:
*
*Input: head = [1,2,3,4]
*Output: [2,1,4,3]
**********************************************************************************/
'''
from SLinkedList import SLinked_List

#Iterative solution, Time complexity  : O(n) Space complexity : O(1)
def swapPairs(head):
    if not head or not head.next:
        return head
    current = head
    previous = None
    index = 0
    while current:
        if index % 2 == 0 and current.next:
            temp = current.next
            if previous:
                previous.next = current.next
                current.next = current.next.next
                temp.next = current
            else:
                current.next = current.next.next
                temp.next = current
                head = temp
            index += 2
        else:
            index += 1
        previous = current
        current = current.next
    return head

#Recursive solution, Time complexity : O(n), Space complexity : O(n)
def swapPairs(head):
    if not head or not head.next:  return head
        
    first_node = head
    second_node = head.next
    
    first_node.next = self.swapPairs(second_node.next)
    second_node.next = first_node
    
    return second_node


elements=[1,2,3,4]

sll=SLinked_List()
sll.add_elements(elements)

print(sll)
swapPairs(sll.head)
print(sll)