'''
Source : https://leetcode.com/problems/implement-strstr/
Author : Yuan Wang
Date   : 2018-06-22

/********************************************************************************** 
*Implement strStr().
*
*Return the index of the first occurrence of needle in haystack, or -1 if needle is 
*not part of haystack.
*
*Example 1:
*
*Input: haystack = "hello", needle = "ll"
*Output: 2
*Example 2:
*
*Input: haystack = "aaaaa", needle = "bba"
*Output: -1
*Clarification:
*
*What should we return when needle is an empty string? This is a great question to 
*ask during an interview.
*
*For the purpose of this problem, we will return 0 when needle is an empty string. 
*This is consistent to C's strstr() and Java's indexOf().
*Time complexity:O(n), Space Complexity:O(1)
**********************************************************************************/
'''

#equal to haystack.find(needle),Time complexity:O(n), Space Complexity:O(1)
def strStr(haystack, needle):
	"""
	:type haystack: str
	:type needle: str
	:rtype: int
	"""
	for i in range(len(haystack)-len(needle)+1):
		if haystack[i:i+len(needle)] == needle:
			return i
	return -1


haystack="hello"
needle="ll"
print(strStr(haystack,needle))
