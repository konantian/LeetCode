
#Source : https://leetcode.com/problems/buddy-strings/
#Author : Yuan Wang
#Date   : 2018-07-01
'''
********************************************************************************** 
*Given two strings A and B of lowercase letters, return true if and only if we can 
*swap two letters in A so that the result equals B.
*
*Example 1:
*
*Input: A = "ab", B = "ba"
*Output: true
*Example 2:**
*
*Input: A = "ab", B = "ab"
*Output: false
*Example 3:
*
*Input: A = "aa", B = "aa"
*Output: true
*Example 4:
*
*Input: A = "aaaaaaabc", B = "aaaaaaacb"
*Output: true
*Example 5:
*
*Input: A = "", B = "aa"
*Output: false
**********************************************************************************/
'''
import collections

def buddyStrings(A, B):
	"""
	:type A: str
	:type B: str
	:rtype: bool
	"""
	
	if not A or not B: return False
	elif len(A) != len(B): return False
	
	elif A==B:
		dic=dict(collections.Counter(A))
		for i in dic:
			if dic[i] > 1:
				return True
		return False
	
	for i in range(len(A)):
		if A[i] != B[i]:
			first=i
	
	for j in range(len(A)-1,-1,-1):
		if A[j] != B[j]:
			second=j
	
	if A[first] == B[second] and B[first] == A[second]:
		return True
	
	return False


A=["aaaaaaabc","abab","ab"]
B=["aaaaaaacb","abab","ab"]

for i in range(len(A)):
	print(buddyStrings(A[i],B[i]))