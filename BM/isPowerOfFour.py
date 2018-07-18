'''
Source : https://leetcode.com/problems/power-of-four/
Author : Yuan Wang
Date   : 2018-07-18

/*************************************************************************************** 
*Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
*
*Example:
*Given num = 16, return true. Given num = 5, return false.
*
*Follow up: Could you solve it without loops/recursion?
****************************************************************************************/
 '''

#Bit manipulation using loop
def isPowerOfFourA(num):
	"""
	:type num: int
	:rtype: bool
	"""
	if num <= 0:
		return False
	
	elif num == 1:
		return True
	
	x = 1
	count = 0
	for i in range(32):
		if num & x:
			count += 1
			if i % 2 != 0:
				return False
	
		x = x << 1
	return count == 1

#Bit manipulation without using loop
def isPowerOfFourB(num):
	"""
	:type num: int
	:rtype: bool
	"""
	return num != 0 and num &(num-1) == 0 and num & 1431655765== num
	#return num > 0 and (num & (num - 1)) == 0 and (num - 1) % 3 == 0
	
print(isPowerOfFourA(16))