#Source : https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
#Author : Yuan Wang
#Date   : 2020-01-10
'''
********************************************************************************** 
*Given the head of a sorted linked list, delete all nodes that have duplicate numbers, 
*leaving only distinct numbers from the original list. Return the linked list sorted as well.
*
*Example 1:
*
*Input: head = [1,2,3,3,4,4,5]
*Output: [1,2,5]
*Example 2:
*
*Input: head = [1,1,1,2,3]
*Output: [2,3]
**********************************************************************************/
'''
from SLinkedList import SLinked_List

def deleteDuplicates(head):
    current = head
    previous = None
    while current and current.next:
        if current.val == current.next.val:
            value = current.val
            temp = current
            while temp and temp.val == value:
                temp = temp.next
            if not previous:
                head = temp
            else:
                previous.next = temp
            current = temp
        else:
            previous = current
            current = current.next
    return head


elements=[1,2,3,3,4,4,5]

sll=SLinked_List()
sll.add_elements(elements)

print(sll)
deleteDuplicates(sll.head)
print(sll)