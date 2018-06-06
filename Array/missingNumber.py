'''
Source : https://leetcode.com/problems/missing-number/
Author : Yuan Wang
Date   : 2018-06-06

/*************************************************************************************** 
 *
 * Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the 
 * one that is missing from the array.
 * 
 * For example,
 * Given nums = [0, 1, 3] return 2.
 * 
 *Example 2:
 *
 *Input: [9,6,4,2,3,5,7,0,1]
 *Output: 8
 * Note:
 * Your algorithm should run in linear runtime complexity. Could you implement it using 
 * only constant extra space complexity?
 * 
 * Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating 
 * all test cases.
 *	   
 ***************************************************************************************/
 '''

#self solution, time complexity: O(n), space complexity: O(1)
def missingNumber(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	total=sum(range(len(nums)+1))
	
	return total-sum(nums)

#Gauss' Formula,sum=n(n+1)/2,takes O(1) to compute the sum
def missingNumberB(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	
	expected_sum = len(nums)*(len(nums)+1)//2
	actual_sum = sum(nums)
	return expected_sum - actual_sum

#HashSet,build a set takes O(n), traverse the list takes O(n),check item in set takes O(1)
#Time complexity: O(n), space complexity O(n)
def missingNumberC(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""

	num_set = set(nums)
	n = len(nums) + 1
	for number in range(n):
		if number not in num_set:
			return number

print(missingNumberC([0,1,3]))