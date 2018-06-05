'''
Source : https://leetcode.com/problems/contains-duplicate-ii/
Author : Yuan Wang
Date   : 2018-06-05

/********************************************************************************** 
 * 
 * Given an array of integers and an integer k, find out whether there there are 
 * two distinct indices i and j in the array such that nums[i] = nums[j] and 
 * the difference between i and j is at most k.
 * 
 *Example 1:

 *Input: nums = [1,2,3,1], k = 3
 *Output: true
 *Example 2:

 *Input: nums = [1,0,1,1], k = 1
 *Output: true
 *Example 3:

 *Input: nums = [1,2,3,1,2,3], k = 2
 *Output: false

 * Time complexity:O(n), it takes O(n) to traverse the list, and takes O(1) to 
 * look up item in dictionary and do minus operations
 * Space complexity:O(n)
 **********************************************************************************/
 '''


def containsNearbyDuplicate(nums, k):
	"""
	:type nums: List[int]
	:type k: int
	:rtype: bool
	"""
	d={}
	for i in range(len(nums)):
		if nums[i] in d and i-d[nums[i]] <= k:
			return True
		d[nums[i]]=i
	return False

print(containsNearbyDuplicate([1,2,3,1,2,1],5))