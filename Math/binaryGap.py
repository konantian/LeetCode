'''
Source : https://leetcode.com/problems/binary-gap/
Author : Yuan Wang
Date   : 2018-07-18

/*************************************************************************************** 
*Given a positive integer N, find and return the longest distance between two consecutive
*1's in the binary representation of N.
*
*If there aren't two consecutive 1's, return 0.
*
*Example 1:
*
*Input: 22
*Output: 2
*Explanation: 
*22 in binary is 0b10110.
*In the binary representation of 22, there are three ones, and two consecutive pairs of 1's.
*The first consecutive pair of 1's have distance 2.
*The second consecutive pair of 1's have distance 1.
*The answer is the largest of these two distances, which is 2.
*Example 2:
*
*Input: 5
*Output: 2
*Explanation: 
*5 in binary is 0b101.
****************************************************************************************/
 '''

def binaryGap(N):
	"""
	:type N: int
	:rtype: int
	"""
	distance=0
	binary=bin(N)[2:]
	found=binary.find("1")

	for i in range(found+1,len(binary)):
		if binary[i] == "1":
			temp=i-found
			found=i
			distance = temp if temp > distance else distance
	
	return distance

N=22
print(binaryGap(N))