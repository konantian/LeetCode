'''
Source : https://leetcode.com/problems/power-of-three/
Author : Yuan Wang
Date   : 2018-07-18

/*************************************************************************************** 
*Given an integer, write a function to determine if it is a power of three.
*
*Example 1:
*
*Input: 27
*Output: true
*Example 2:
*
*Input: 0
*Output: false
*Example 3:
*
*Input: 9
*Output: true
****************************************************************************************/
 '''
#Self solution
def isPowerOfThree(n):
	"""
	:type n: int
	:rtype: bool
	"""
	
	if n <= 0:
		return False
	
	while(n>1):
	
		if n % 3 != 0:
			return False
		n=n//3

	return True

#Other solution
def isPowerOfThree(n):
	"""
	:type n: int
	:rtype: bool
	"""

	return n > 0 and 1162261467 % n == 0

n=27
print(isPowerOfThree(n))