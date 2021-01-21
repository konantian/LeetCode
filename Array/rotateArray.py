'''
Source : https://leetcode.com/problems/rotate-array/
Author : Yuan Wang
Date   : 2018-06-04

/********************************************************************************** 
* 
* Rotate an array of n elements to the right by k steps.
* For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4]. 
* 
*Example 1:
* 
* Input: [-1,-100,3,99] and k = 2
* Output: [3,99,-1,-100]
* Explanation: 
* rotate 1 steps to the right: [99,-1,-100,3]
* rotate 2 steps to the right: [3,99,-1,-100]
* Note:
* Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
* 
* Hint:
* Could you do it in-place with O(1) extra space?
* 
* Related problem: Reverse Words in a String II
* 
* 
*	   
**********************************************************************************/
'''
def rotateA(nums, k):
	"""
	:type nums: List[int]
	:type k: int
	:rtype: void Do not return anything, modify nums in-place instead.
	"""
	n = len(nums)
	nums[:] = nums[n-k:] + nums[:n-k]

def rotateB(nums, k):
	"""
	:type nums: List[int]
	:type k: int
	:rtype: void Do not return anything, modify nums in-place instead.
	"""
	
	if len(nums) != k:
		for i in range(k):
			element=nums.pop()
			nums.insert(0,element)

def rotateC(nums, k):
	"""
	:type nums: List[int]
	:type k: int
	:rtype: void Do not return anything, modify nums in-place instead.
	"""
	temp=[]
	for i in range(len(nums)):
		temp.append(0)
	for i in range(len(nums)):
		temp[(i+k) % len(nums)]=nums[i]
	for i in range(len(nums)):
		nums[i]=temp[i]
nums=[1,2]
k=10
rotateA(nums,3)
print(nums)