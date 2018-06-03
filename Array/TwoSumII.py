'''
Source : https://oj.leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Author : Yuan Wang
Date   : 2018-06-03

/********************************************************************************** 
* 
* Given an array of integers that is already sorted in ascending order, 
* find two numbers such that they add up to a specific target number.
* 
* The function twoSum should return indices of the two numbers such that they add up to the target, 
* where index1 must be less than index2. Please note that your returned answers (both index1 and index2) 
* are not zero-based.
* 
* You may assume that each input would have exactly one solution.
* 
* Input: numbers={2, 7, 11, 15}, target=9
* Output: [1,2]
* Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
**********************************************************************************/
'''
#two pointers
def twoSum(numbers, target):
	"""
	:type numbers: List[int]
	:type target: int
	:rtype: List[int]
	"""

	left,right=0,len(numbers)-1
	while left < right:
		s=numbers[left]+numbers[right]
		if s == target:
			return [left+1,right+1]
		elif s < target:
			left += 1
		else:
			right -= 1

# binary search	
def twoSumB(numbers, target):
	for i in xrange(len(numbers)):
		l, r = i+1, len(numbers)-1
		tmp = target - numbers[i]
		while l <= r:
			mid = l + (r-l)//2
			if numbers[mid] == tmp:
				return [i+1, mid+1]
			elif numbers[mid] < tmp:
				l = mid+1
			else:
				r = mid-1
