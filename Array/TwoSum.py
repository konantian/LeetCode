
#Source : https://oj.leetcode.com/problems/two-sum/
#Author : Yuan Wang
#Date   : 2018-05-26
'''
********************************************************************************** 
* 
* Given an array of integers, find two numbers such that they add up to a specific target number.
* 
* The function twoSum should return indices of the two numbers such that they add up to the target, 
* where index1 must be less than index2. Please note that your returned answers (both index1 and index2) 
* are not zero-based.
* 
* You may assume that each input would have exactly one solution.
* 
* Input: numbers={2, 7, 11, 15}, target=9
* Output: index1=1, index2=2
* 
*	   
**********************************************************************************/
'''

'''
Complexity Analysis

Time complexity : O(n^2). For each element, we try to find its complement by looping 
through the rest of array which takes O(n)O(n) time. 
Therefore, the time complexity is O(n^2)O(n^2).

Space complexity : O(1)O(1).
'''
def twoSum(nums, target):
	"""
	:type nums: List[int]
	:type target: int
	:rtype: List[int]
	"""
	for i in range(len(nums)):
		for j in range(i+1,len(nums)):
			if nums[i]+nums[j]==target:
				return [i,j]


#python dict using hash table to find, it takes O(1) to check,takes O(n) to iterate
#all elements in array
def twoSumB(nums,target):
	if len(nums) <= 1:
		return False
	buff_dict = {}
	for i in range(len(nums)):
		if nums[i] in buff_dict:
			return [buff_dict[nums[i]], i]
		else:
			buff_dict[target - nums[i]] = i

print(twoSumB([3,2,4],6))