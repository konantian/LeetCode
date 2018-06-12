'''
Source : https://leetcode.com/problems/maximum-average-subarray-i/
Author : Yuan Wang
Date   : 2018-06-12

/*************************************************************************************** 
*Given an array consisting of n integers, find the contiguous subarray of given length
*k that has the maximum average value. And you need to output the maximum average value.

*Example 1:
*Input: [1,12,-5,-6,50,3], k = 4
*Output: 12.75
*Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

 ****************************************************************************************
 '''
#Time complexity: O(n), Space complexity:O(1)
def findMaxAverage(nums, k):
	"""
	:type nums: List[int]
	:type k: int
	:rtype: float
	"""
	if len(nums) == k:
		return sum(nums)/k
	
	first=0
	temp=total=sum(nums[:k])
	for i in range(k,len(nums)):
		temp=temp-nums[first]+nums[i]
		total = temp if temp > total else total
		first+=1
	return total/k

nums=[1,12,-5,-6,50,3]
k=4
print(findMaxAverage(nums,k))