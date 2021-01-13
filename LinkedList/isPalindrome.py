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
	# rev records the first half, need to set the same structure as fast, slow, hence later we have rev.next
    rev = None
    # initially slow and fast are the same, starting from head
    slow = fast = head
    while fast and fast.next:
        # fast traverses faster and moves to the end of the list if the length is odd
        fast = fast.next.next
        
        # take it as a tuple being assigned (rev, rev.next, slow) = (slow, rev, slow.next), hence the re-assignment of slow would not affect rev (rev = slow)
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
       # fast is at the end, move slow one step further for comparison(cross middle one)
        slow = slow.next
    # compare the reversed first half with the second half
    while rev and rev.val == slow.val:
        slow = slow.next
        rev = rev.next
    
    # if equivalent then rev become None, return True; otherwise return False 
    return not rev

elements=[1,2,3,4,3,2,1]

sll=SLinked_List()
sll.add_elements(elements)
print(sll)
print(isPalindromeB(sll.head))
