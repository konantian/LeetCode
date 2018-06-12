'''
Source : https://leetcode.com/problems/maximum-product-of-three-numbers/
Author : Yuan Wang
Date   : 2018-06-11

/**********************************************************************************
Given an integer array, find three numbers whose product is 
maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6
Example 2:
Input: [1,2,3,4]
Output: 24
**********************************************************************************/
'''
#self solution, sort the array first and iterate each subarray of size 3 to get the
#maximum product, Time complexity:O(nlogn),Space complexity:O(1)
def maximumProduct(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	nums=sorted(nums,reverse=True)
	number=1
	n=len(nums)
	if nums[-1] >= 0 or len(nums)==3:
		for i in range(3):
			number*=nums[i]
	
		return number
	else:
		for i in range(n):
			result=nums[i]*nums[(i+1)%n]*nums[(i+2)%n]
			number = result if result > number else number
	
		return number

#other solution, sor the array first, the maximum product of three elements has only two 
#possible way, one is the three number are the largest three or the positive one is the
#largest with two smallest negative numbers,compare them and return the larger one
#Time complexity:O(nlogn), Space complexity:O(1)
def maximumProduct(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	nums = sorted(nums)
	first_option=nums[0]*nums[1]*nums[-1]
	second_option=nums[-3] * nums[-2] * nums[-1]
	
	return first_option if first_option > second_option else second_option

nums=[-3,0,-1,-2,4,3,5]
print(maximumProduct(nums))