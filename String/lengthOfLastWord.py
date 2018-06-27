
#Source : https://leetcode.com/problems/length-of-last-word/
#Author : Yuan Wang
#Date   : 2018-06-27
'''
********************************************************************************** 
*Given a string s consists of upper/lower-case alphabets and empty space characters
*' ', return the length of last word in the string.
*
*If the last word does not exist, return 0.
*
*Note: A word is defined as a character sequence consists of non-space characters only.
*
*Example:
*
*Input: "Hello World"
*Output: 5
**********************************************************************************/
'''

#Pythonic
def lengthOfLastWord(s):
	"""
	:type s: str
	:rtype: int
	"""
	if not s:
		return 0
	try:
		return len(s.split()[-1])
	except:
		return 0

#Self solution,using list comprehension, list the indexes of all characters that are not empty
#find the point that the index are not continuous and use the last index of that list to minor
#the current position,Time complexity:O(n), Space complexity:O(1)
def lengthOfLastWord(s):
	"""
	:type s: str
	:rtype: int
	"""
	index_list=[i for i in range(len(s)) if s[i] != " "]
	if not index_list:
		return 0
	
	for i in range(len(index_list)-1,-1,-1):
		if index_list[i]-1 != index_list[i-1]:
			return index_list[-1]-index_list[i]+1


s="  Hello world   "
print(lengthOfLastWord(s))