'''
Source : https://oj.leetcode.com/problems/maximum-subarray/
Author : Yuan Wang
Date   : 2018-05-28

/********************************************************************************** 
* 
* Find the contiguous subarray within an array (containing at least one number) 
* which has the largest sum.
* 
* For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
* the contiguous subarray [4,−1,2,1] has the largest sum = 6.
* 
* More practice:
* 
* If you have figured out the O(n) solution, try coding another solution using 
* the divide and conquer approach, which is more subtle.
* 
*               
**********************************************************************************/
'''

array=[-2,1,-3,4,-1,2,1,-5,4]
#array=[4,-1,2]
#array=[-1,-2]
def maxSubArray(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	maxSoFar=nums[0]
	maxEndingHere=nums[0]
	for i in range(1,len(nums)):
		maxEndingHere=max(maxEndingHere+nums[i],nums[i])
		maxSoFar=max(maxSoFar,maxEndingHere)
		print(maxEndingHere,maxSoFar)

	return maxSoFar

def maxSubArrayB(nums):
	total=nums[0]
	if len(nums) == 1:
		return nums[0]
	for i in range(len(nums)):
		for j in range(1,len(nums)+1):
			sub_array=nums[i:j]
			if len(sub_array) != 0:
				sum_array=sum(sub_array)
				if sum_array > total:
					total=sum_array
	return total

#DP, to check previous sum, reset it to 0 if it's less than 0
#O(n-1) time, O(1) space
def maxSubArrayC(nums):
	res=nums[0]
	sum_array=nums[0]
	for i in range(1,len(nums)):
		sum_array=max(sum_array,0)+nums[i]
		res=max(res,sum_array)
		print(sum_array,res)
	return res
print(maxSubArrayC(array))
