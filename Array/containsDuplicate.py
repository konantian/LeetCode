'''
Source : https://leetcode.com/problems/contains-duplicate/
Author : Yuan Wang
Date   : 2018-06-05

/********************************************************************************** 
 * 
 * Given an array of integers, find if the array contains any duplicates. 
 * Your function should return true if any value appears at least twice in the array, 
 * and it should return false if every element is distinct.
 *	   
 * Complexity Analysis

Time complexity : O(n). We only traverse the list once and look up item in dictionary takes O(1)

Space complexity : O(n). The space used by creating a dictionary
 **********************************************************************************/
 '''

#AC but slowly
from random import*

def containsDuplicateA(nums):
	"""
	:type nums: List[int]
	:rtype: bool
	"""
	if not nums:
		return False
	d=dict(collections.Counter(nums))
	for i in d:
		if d[i] >=2:
			return True
	return False

#AC, faster using hash,O(n)
def containsDuplicateB(nums):
	"""
	:type nums: List[int]
	:rtype: bool
	"""
	if not nums:
		return False
	d={}
	for i in nums:
		if i in d:
			return True
		else:
			d[i] = True
	return False
'''
using set in python to remove duplicate elements and detect the length of set and 
original list,if same lenght means no duplicate, vice versa
set are build by hash table,convert a list to set takes O(n), obtain the length of set
takes O(1), in total, takes O(n) to check if duplicate

'''
def containsDuplicateC(nums):
	"""
	:type nums: List[int]
	:rtype: bool
	"""
	n=len(nums)  #len(list) takes O(1)
	if n < 2 or not nums:
		return False
	return True if len(set(nums)) < n else False

#sort takes O(nlogn), traverse the list takes O(n),in total
#O(nlogn+n) which is O(nlogn)
def containsDuplicateD(nums):
	"""
	:type nums: List[int]
	:rtype: bool
	"""

	nums.sort()
	for i in range(1,len(nums)):
		if nums[i] == nums[i-1]:
			return True

	return False
#nums=sample(range(-10,10),randint(0,10))
nums=[1,2,3]
print(containsDuplicateD(nums))
	