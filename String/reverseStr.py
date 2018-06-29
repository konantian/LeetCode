
#Source : https://leetcode.com/problems/reverse-string-ii/
#Author : Yuan Wang
#Date   : 2018-06-29
'''
********************************************************************************** 
*Given a string and an integer k, you need to reverse the first k characters for 
*every 2k characters counting from the start of the string. If there are less than 
*k characters left, reverse all of them. If there are less than 2k but greater than 
*or equal to k characters, then reverse the first k characters and left the other as 
*original.
*Example:
*Input: s = "abcdefg", k = 2
*Output: "bacdfeg"
**********************************************************************************/
'''

#Self solution, Time complexity:O(n) Space complexity:O(n)
def reverseStrA(s, k):
	"""
	:type s: str
	:type k: int
	:rtype: str
	"""
	if len(s) <=k:
		return s[::-1]
	elif k<=len(s)<2*k:
		return s[:k][::-1]+s[k:]
	else:
		result=""
		start=0
		value=len(s) % (2 * k)
		if value != 0:
			s+=" "*(2*k-value)
		for i in range(2*k-1,len(s),2*k):
			string=s[start:i+1]
			substring=string[:k]
			result+=substring[::-1]+string[k:]
			start=i+1
	
	return result.replace(" ","")

#solution
def reverseStrB(s, k):
	"""
	:type s: str
	:type k: int
	:rtype: str
	"""
	result=""
	start=0
	for i in range(0,len(s),2*k):
		string=s[i:i+k]
		result+=string[::-1]+s[i+k:i+2*k]

	return result

s="abcdefg"
k=2
print(reverseStr(s,k))