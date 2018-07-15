'''
Source : https://leetcode.com/problems/valid-parentheses/
Author : Yuan Wang
Date   : 2018-07-15

/*************************************************************************************** 
*Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine
*if the input string is valid.
*
*An input string is valid if:
*
*Open brackets must be closed by the same type of brackets.
*Open brackets must be closed in the correct order.
*Note that an empty string is also considered valid.
*
*Example 1:
*
*Input: "()"
*Output: true
*Example 2:
*
*Input: "()[]{}"
*Output: true
*Example 3:
*
*Input: "(]"
*Output: false
****************************************************************************************/
 '''

 #Self solution,Time complexity:O(n) Space complexity:O(n)
def isValid(s):
	"""
	:type s: str
	:rtype: bool
	"""
	if not s:
		return True
	
	if len(s) % 2 != 0:
		return False
	
	keys=["(","[","{"];values=[")","]","}"]
	pair_dict=dict(zip(keys+values,values+keys))
	
	import collections
	dic_count=dict(collections.Counter(s))
	for i in dic_count:
		try:
			if  dic_count[i] != dic_count[pair_dict[i]]:
				return False
		except:
			return False
	
	dic_index={i:[x for x,char in enumerate(s) if char == i] for i in dic_count}
	
	for i in dic_index:
		two_count=0
		n=len(dic_index[i])
		for x in range(n):
			if abs(dic_index[i][x]-dic_index[pair_dict[i]][n-x-1]) % 2 == 0:
				two_count+=1

		if two_count % 2 != 0:
			return False
	
	return True

#Other simple solution
def isValidB(s):
	d = {'{':'}', '(':')', '[':']'}
	q = []
	for c in s:
		if c in d:
			q.append(c)
		elif not q or c != d[q.pop()]:
			return False
	return not q

s="(([]){})"
print(isValid(s))
