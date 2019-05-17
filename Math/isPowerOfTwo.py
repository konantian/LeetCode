'''
Source : https://leetcode.com/problems/power-of-two/description/
Author : Yuan Wang
Date   : 2018-07-14

/*************************************************************************************** 
*Given an integer, write a function to determine if it is a power of two.
*
*Example 1:
*
*Input: 1
*Output: true 
*Explanation: 20 = 1
*Example 2:
*
*Input: 16
*Output: true
*Explanation: 24 = 16
*Example 3:
*
*Input: 218
*Output: false   
****************************************************************************************/
 '''

#Time complexity:O(logn)
def isPowerOfTwo(n):
	"""
	:type n: int
	:rtype: bool
	"""
	if n <= 0:
		return False
	
	while(n>1):
	
		if n % 2 != 0:
			return False
		n=n//2

	return True

#Bitwise operation
def isPowerOfTwo(self, n: int) -> bool:
    return (n != 0) and ((n & (n-1)) == 0)

n=218
print(isPowerOfTwo(n))