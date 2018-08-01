#Source : https://leetcode.com/problems/linked-list-cycle/
#Author : Yuan Wang
#Date   : 2018-08-01
'''
********************************************************************************** 
*Given a linked list, determine if it has a cycle in it.
*
*Follow up:
*Can you solve it without using extra space?
**********************************************************************************/
'''

#Self solution, Time complexity:O(n) Space complexity:O(n)
def hasCycle(self, head):
	"""
	:type head: ListNode
	:rtype: bool
	"""
	if not head:
		return False
	dic={}
	
	current=head
	while current != None:
		if current not in dic:
			dic[current]=False
		else:
			return True
		current=current.next
	
	return False

'''
Other solution, Time complexity:O(n) Space complexity:O(1)
Algorithm

The space complexity can be reduced to O(1)O(1) by considering two pointers at different speed
 - a slow pointer and a fast pointer. The slow pointer moves one step at a time while the 
 fast pointer moves two steps at a time.

If there is no cycle in the list, the fast pointer will eventually reach the end and we can 
return false in this case.

Now consider a cyclic list and imagine the slow and fast pointers are two runners racing around 
a circle track. The fast runner will eventually meet the slow runner. Why? Consider this case 
(we name it case A) - The fast runner is just one step behind the slow runner. In the next iteration,
 they both increment one and two steps respectively and meet each other.

How about other cases? For example, we have not considered cases where the fast runner is two or 
three steps behind the slow runner yet. This is simple, because in the next or next's next iteration,
this case will be reduced to case A mentioned above.
'''

def hasCycle(self, head):
	"""
	:type head: ListNode
	:rtype: bool
	"""
	try:
		slow = head
		fast = head.next
		while slow is not fast:
			slow = slow.next
			fast = fast.next.next
		return True
	except:
		return False
