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

	if num & (num-1) != 0:
		return False

	total = 0
	while num > 1:
		total += 1
		num = num >> 1
  
	return total & 1 == 0

#Bit manipulation without using loop
def isPowerOfFourB(num):
	"""
	:type num: int
	:rtype: bool
	"""
	return num != 0 and num &(num-1) == 0 and num & 1431655765== num
	#return num > 0 and (num & (num - 1)) == 0 and (num - 1) % 3 == 0
	
print(isPowerOfFourA(16))