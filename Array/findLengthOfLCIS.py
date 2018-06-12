'''
Source : https://leetcode.com/problems/longest-continuous-increasing-subsequence/
Author : Yuan Wang
Date   : 2018-06-12

/*************************************************************************************** 
*Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).
*
*Example 1:
*Input: [1,3,5,4,7]
*Output: 3
*Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
*Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 
*Example 2:
*Input: [2,2,2,2,2]
*Output: 1
*Explanation: The longest continuous increasing subsequence is [2], its length is 1. 
*
*****************************************************************************************
 '''

#Time complexity:O(n), Space complexity:O(1)
def findLengthOfLCIS(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	if not nums:
		return 0
	first=second=1
	for i in range(1,len(nums)):
		if nums[i] > nums[i-1]:
			second+=1
		else:
			second=1
		first = second if second > first else first
	return first

nums=[1,2,3,4,6,5,7,8,9,10,11]
print(findLengthOfLCIS(nums))