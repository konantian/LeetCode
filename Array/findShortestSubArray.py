'''
Source : https://leetcode.com/problems/degree-of-an-array/
Author : Yuan Wang
Date   : 2018-06-15

/********************************************************************************** 
* 
*Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
*
*Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
*
*Example 1:
*Input: [1, 2, 2, 3, 1]
*Output: 2
*Explanation: 
*The input array has a degree of 2 because both elements 1 and 2 appear twice.
*Of the subarrays that have the same degree:
*[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
*The shortest length is 2. So return 2.
*Example 2:
*Input: [1,2,2,3,1,4,2]
*Output: 6
* 
* 
*	   
**********************************************************************************/
'''

#Time complexity:O(n), Space complexity:O(n)
def findShortestSubArray(self, nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	d={}
	for i,num in enumerate(nums):
		if num not in d:
			d[num]=[i]
		else:
			d[num].append(i)
	element=float('inf')
	max_length=max(collections.Counter(nums).values())
	#for i in d:
        #max_length = len(d[i]) if len(d[i])>max_length else max_length
	for i in d:
		if len(d[i])==max_length:
			length=d[i][-1]-d[i][0]
			element=length if length<element else element
	return element+1

nums=[1,2,2,3,1,4,2]
print(findShortestSubArray(nums))