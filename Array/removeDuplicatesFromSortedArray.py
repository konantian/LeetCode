#Author : Yuan Wang
#Date   : 2018-05-26

#********************************************************************************** 
# 
# Given a sorted array, remove the duplicates in place such that each element appear 
# only once and return the new length.
# 
# Do not allocate extra space for another array, you must do this in place with constant memory.
# 
# For example,
# Given input array A = [1,1,2],
# 
# Your function should return length = 2, and A is now [1,2].
# 
#	   
#**********************************************************************************/

#worked well with less time,accepted by the leetcode.com
def removeDuplicatesA(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	k=0  
	for i in range(1,len(nums)):  
		if nums[i] != nums[k]:  
			k+=1  
			nums[k] = nums[i]  
	  
	#del nums[k+1:len(nums)]

	return k+1

#worked well but slow for large array	
def removeDuplicatesB(nums):
	for i in nums:
		repeat=nums.count(i)
		if repeat > 1:
			for j in range(repeat-1):
				nums.remove(i)

	return len(nums)
#worked well but slow for large array	
def removeDuplicatesC(nums):
	for i in nums:
		while(nums.count(i)>1):
			nums.remove(i)
	return len(nums)

A=[1,1,2,3,3,3,4,4,5]
count=removeDuplicatesA(A)
print(count)
