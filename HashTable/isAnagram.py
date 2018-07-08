
#Source : https://leetcode.com/problems/valid-anagram/
#Author : Yuan Wang
#Date   : 2018-07-08
'''
********************************************************************************** 
*Given two strings s and t , write a function to determine if t is an anagram of s.
*
*Example 1:
*
*Input: s = "anagram", t = "nagaram"
*Output: true
*Example 2:
*
*Input: s = "rat", t = "car"
*Output: false
*Note:
*You may assume the string contains only lowercase alphabets.
*
*Follow up:
*What if the inputs contain unicode characters? How would you adapt your solution to such case?
**********************************************************************************/
'''
'''
Pythonic using dictionary
Complexity analysis

Time complexity : O(n). Time complexity is O(n) because 
accessing the counter table is a constant time operation.

Space complexity : O(1). Although we do use extra space, 
the space complexity is O(1) because the table's size 
stays constant no matter how large nn is.
'''
def isAnagramA(s, t):
	"""
	:type s: str
	:type t: str
	:rtype: bool
	"""
	dic_s=dict(collections.Counter(s))
	dic_t=dict(collections.Counter(t))
	
	return dic_s == dic_t

'''
Complexity analysis

Time complexity : O(nlogn). Assume that nn is the 
length of ss, sorting costs O(nlogn) and comparing 
two strings costs O(n). Sorting time dominates and the 
overall time complexity is O(nlogn).

Space complexity : O(1). Space depends on the sorting implementation 
which, usually, costs O(1) auxiliary space if heapsort is used. Note 
that in Java, toCharArray() makes a copy of the string so it costs O(n) 
extra space, but we ignore this for complexity analysis because:
'''

def isAnagramB(s, t):
	"""
	:type s: str
	:type t: str
	:rtype: bool
	"""
	s=sorted(s)
	t=sorted(t)
	
	return s == t

s = "anagram"
t = "nagaram"
print(isAnagramA(s,t))

