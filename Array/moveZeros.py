'''
Source : https://leetcode.com/problems/move-zeroes/
Author : Yuan Wang
Date   : 2018-06-07

/*************************************************************************************** 
 *
 * Given an array nums, write a function to move all 0's to the end of it while 
 * maintaining the relative order of the non-zero elements.
 *
 * For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should
 * be [1, 3, 12, 0, 0].
 * 
 * Note:
 * You must do this in-place without making a copy of the array.
 * Minimize the total number of operations.
 * 
 * Credits:
 * Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
 *	   
 ***************************************************************************************/
 '''
 #count takes O(n) remove 0 takes O(n), append 0 to the end takes O(1)
 #Time complexity:O(n), space complexity: O(1)
 def moveZeroesA(nums):
	"""
	:type nums: List[int]
	:rtype: void Do not return anything, modify nums in-place instead.
	"""
	count=nums.count(0)
	nums[:]=[i for i in nums if i != 0]  #using nums[:] + list comprehension can modify the list in place
										#without extra space
	nums+=[0]*count						#using += can append the element to the end or front of the list with O(1)

#modify my solution to one solution,still O(n), but much faster for large n
 def moveZeroesA_modify(nums):
	"""
	:type nums: List[int]
	:rtype: void Do not return anything, modify nums in-place instead.
	"""

	nums[:]=[i for i in nums if i !=0 ] + [x for x in nums if x == 0]

def moveZeroesB(nums):
	"""
	:type nums: List[int]
	:rtype: void Do not return anything, modify nums in-place instead.
	"""
	nonzeroes = [x for x in nums if x != 0]
	if nonzeroes and len(nonzeroes) < len(nums):
		nums[:len(nonzeroes)] = nonzeroes
		nums[len(nonzeroes):] = [0] * (len(nums) - len(nonzeroes))

def moveZeroesC(nums):
	"""
	:type nums: List[int]
	:rtype: void Do not return anything, modify nums in-place instead.
	"""
	moveIndex = 0
	for i in range(0,len(nums)):
		if nums[i]:
		temp = nums[moveIndex]
		nums[moveIndex] = nums[i]
		nums[i] = temp
		moveIndex +=1
	
	