
#Source : https://leetcode.com/problems/valid-palindrome/
#Author : Yuan Wang
#Date   : 2018-06-23
'''
********************************************************************************** 
*Given a string, determine if it is a palindrome, considering only alphanumeric 
*characters and ignoring cases.
*
*Note: For the purpose of this problem, we define empty string as valid palindrome.
*
*Example 1:
*
*Input: "A man, a plan, a canal: Panama"
*Output: true
*Example 2:
*
*Input: "race a car"
*Output: false   
**********************************************************************************/
'''

#Pythonic,self-solution, Time complexity:O(n),Space complexity:O(n)
def isPalindrome(s):
	"""
	:type s: str
	:rtype: bool
	"""
	s=s.lower()
	element=[i for i in s if i.isalnum()]
 
	return element==element[::-1]


#Two pointer
def isPalindrome(s):
	"""
	:type s: str
	:rtype: bool
	"""
	l, r = 0, len(s) - 1
	while l < r:
		if not s[l].isalnum():
			l += 1
		elif not s[r].isalnum():
			r -= 1
		else:
			if s[l].lower() != s[r].lower():
				return False
			else:
				l += 1
				r -= 1
	return True
s="A man, a plan, a canal: Panama"
print(isPalindrome(s))