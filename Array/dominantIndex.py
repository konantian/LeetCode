'''
Source : https://leetcode.com/problems/largest-number-at-least-twice-of-others/
Author : Yuan Wang
Date   : 2018-06-13

/**********************************************************************************
In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

Example 1:

Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.
 

Example 2:

Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.

Time complexity:O(n), Space complexity:O(1)
**********************************************************************************/
'''

def dominantIndex(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	number=max(nums)
	for i,num in enumerate(nums):
		if num == number:
			index=i
		if num>float(number/2) and num != number:
			return -1
	return index

def dominantIndex(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	if len(nums) == 1:
		return 0
	number=max(nums)
	index=nums.index(number)
	nums.remove(number)
	return index if number>=max(nums)*2 else -1
 
nums=[3,6,1,0]
print(dominantIndex(nums))
