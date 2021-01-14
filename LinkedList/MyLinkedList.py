#Source : https://leetcode.com/problems/design-linked-list/
#Author : Yuan Wang
#Date   : 2021-01-14
'''
********************************************************************************** 
*Design your implementation of the linked list. You can choose to use a singly or 
*doubly linked list.
*A node in a singly linked list should have two attributes: val and next. val is 
*the value of the current node, and next is a pointer/reference to the next node.
*If you want to use the doubly linked list, you will need one more attribute prev 
*to indicate the previous node in the linked list. Assume all nodes in the linked 
*list are 0-indexed.
**********************************************************************************/
'''


class ListNode:
	def __init__(self, val=0, next=None):
		self.val=val
		self.next=next

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size: return -1
        pos = 0
        current = self.head
        while current and pos <= index:
            if pos == index:
                return current.val
            current = current.next
            pos += 1
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        temp = ListNode(val, self.head)
        self.head = temp
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        temp = ListNode(val)
        if not self.head:
            self.head = temp
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = temp
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        
        if index == 0:
            self.addAtHead(val)
            return
            
        temp = ListNode(val)
        current = self.head
        previous = None
        pos = 0
        found = False

        while not found:
            if pos == index:
                found = True
                self.size += 1
            else:
                previous = current
                current=current.next
                pos += 1
        if self.head == None:
            self.head = temp

        else :
            temp.next = current
            if index == 0:
                self.head = temp
            else:
                previous.next = temp
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        
        if not self.head: return
        
        pos = 0
        current = self.head
        found = False
        previous = None
        while pos <= index and current and not found:
            if pos == index:
                found = True
                self.size -= 1
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
            else:
                previous = current
                pos += 1
                current = current.next