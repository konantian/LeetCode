'''
Source : https://leetcode.com/problems/rotate-array/
Author : Yuan Wang
Date   : 2018-06-04

/********************************************************************************** 
* 
* Rotate an array of n elements to the right by k steps.
* For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4]. 
* 
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
nums=[1,2,3,4,5,6,7]
k=3
rotateC(nums,3)
print(nums)