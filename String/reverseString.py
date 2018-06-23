
#Source : https://leetcode.com/problems/reverse-string/
#Author : Yuan Wang
#Date   : 2018-06-23
'''
********************************************************************************** 
*Write a function that takes a string as input and returns the string reversed.
*
*Example:
*Given s = "hello", return "olleh".
**********************************************************************************/
'''

#Pythonic, Time complexity:O(n), Space complexity:O(1)
def reverseString(s):
	"""
	:type s: str
	:rtype: str
	"""
	return s[::-1]



#Self solution, Time complexity:O(n), Space complexity:O(n)
def reverseString(s):
	"""
	:type s: str
	:rtype: str
	"""
	result=""
	for i in range(len(s)-1,-1,-1):
		result+=s[i]
	
	return result

#swap the end element and the front element until the swap ending
def reverseString(s):
	"""
	:type s: str
	:rtype: str
	"""
	r = list(s)
	i, j  = 0, len(r) - 1
	while i < j:
		r[i], r[j] = r[j], r[i]
		i += 1
		j -= 1

	return "".join(r)
print(reverseString("HelloWorld"))