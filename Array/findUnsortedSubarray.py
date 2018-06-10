'''
Source : https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
Author : Yuan Wang
Date   : 2018-06-10

Given an integer array, you need to find one continuous subarray that if
you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
'''

#Time complexity:O(n), Space complexity:O(1)
def findUnsortedSubarray(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	n=len(nums)
	start=-1
	end=-2
	small=nums[n-1]
	big=nums[0]
	for i in range(1,n):
		big = nums[i] if big < nums[i] else big
		small = nums[n-1-i] if small > nums[n-1-i] else small
		if nums[i] < big:
			end=i
		if nums[n-1-i] > small:
			start=n-1-i
	
	return end-start+1

#Time complexity:O(nlog), Space complexity:O(n)
def findUnsortedSubarray(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	copy=nums.copy()
	nums.sort()
	start=-1
	end=-1
	for i in range(len(nums)):
		if nums[i] != copy[i]:
			if start == -1:
				start=i
			else:
				end=i
	return 0 if end ==-1 and start == -1 else end-start+1