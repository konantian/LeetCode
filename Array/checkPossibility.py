'''
Source : https://leetcode.com/problems/non-decreasing-array/
Author : Yuan Wang
Date   : 2018-06-16

/********************************************************************************** 
*Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.
*
*We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).
8
*Example 1:
*Input: [4,2,3]
*Output: True
*Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
*
*Example 2:
*Input: [4,2,1]
*Output: False
*Explanation: You can't get a non-decreasing array by modify at most one element.
**********************************************************************************/
'''

def check_order(numbers):
	for i in range(1,len(numbers)):
		if numbers[i]<numbers[i-1]:
			return False
	
	return True

#Find the element that not in order, and test if remove it, the
#remain list are still sorted, if sorted, which means modify at
#most 1 time can make the array non-decreasing. Otherwise, the
#remain list are not sorted, just return False
def checkPossibility(nums):
	"""
	:type nums: List[int]
	:rtype: bool
	"""
	if not nums or len(nums)==1:
		return True
	for i in range(1,len(nums)):
		if nums[i] < nums[i-1]:
			temp=nums[:i-1]+nums[i:]
			option=nums[:i]+nums[i+1:]
			if check_order(temp) or check_order(option):
				return True
			else:
				return False
	return True

nums=[2,3,3,2,4]
print(checkPossibility(nums))

