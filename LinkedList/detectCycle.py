#Source : https://leetcode.com/problems/linked-list-cycle-ii/
#Author : Yuan Wang
#Date   : 2018-08-01
'''
********************************************************************************** 
*Given a linked list, return the node where the cycle begins. If there is no cycle,
*return null.
*
*Note: Do not modify the linked list.
*
*Follow up:
*Can you solve it without using extra space?
**********************************************************************************/
'''

#Self solution, Time complexity:O(n) Space complexity:O(n)
def detectCycle(self, head):
	"""
	:type head: ListNode
	:rtype: ListNode
	"""
	if not head:
		return None
	dic={}
	
	current=head
	while current != None:
		if current not in dic:
			dic[current]=False
		else:
			return current
		current=current.next
	return None

#Other solution, Time complexity:O(n) Space complexity:O(1)
def detectCycle(self, head):
	"""
	:type head: ListNode
	:rtype: ListNode
	"""
	if head == None or head.next == None:
		return None
	slow = head
	fast = head
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
		if slow == fast:
			break
	if slow == fast:
		slow = head
		while slow != fast:
			slow = slow.next
			fast = fast.next
		return slow
	return None