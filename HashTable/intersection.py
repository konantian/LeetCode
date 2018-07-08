
#Source : https://leetcode.com/problems/intersection-of-two-arrays/
#Author : Yuan Wang
#Date   : 2018-07-07
'''
********************************************************************************** 
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
**********************************************************************************/
'''

#Pythonic solution,Time complexity:O(n), Space complexity:O(n)
def intersection(nums1, nums2):
	"""
	:type nums1: List[int]
	:type nums2: List[int]
	:rtype: List[int]
	"""
	nums1=set(nums1)
	nums2=set(nums2)
	
	return list(nums1.intersection(nums2))


nums1=[1,2,2,1]
nums2=[2,2]
print(intersection(nums1,nums2))