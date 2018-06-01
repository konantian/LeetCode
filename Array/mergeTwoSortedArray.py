'''
Source : https://oj.leetcode.com/problems/merge-sorted-array/
Author : Yuan Wang
Date   : 2018-06-01

/********************************************************************************** 
* 
* Given two sorted integer arrays A and B, merge B into A as one sorted array.
* 
* Note:
*   You may assume that A has enough space (size that is greater or equal to m + n) 
*   to hold additional elements from B. The number of elements initialized in A and B 
*   are m and n respectively.
*	
*	
**********************************************************************************/
'''
#Time complexity:O(nlogn) Space complexity:O(n)
def merge(nums1, m, nums2, n):
	"""
	:type nums1: List[int]
	:type m: int
	:type nums2: List[int]
	:type n: int
	:rtype: void Do not return anything, modify nums1 in-place instead.
	"""
	nums1[m:]=nums2
	nums1.sort()

#Time complexity: O(n) Space complexity: O(1)
def merge2(nums1,m,nums2,n):

	i=m-1
	j=n-1
	k=m+n-1
	while(i>=0 and j>=0):
		if nums1[i] > nums2[j]:
			nums1[k]=nums1[i]
			k-=1
			i-=1
		else:
			nums1[k]=nums2[j]
			k-=1
			j-=1

	while(j>=0):
		nums1[k]=nums2[j]
		k-=1
		j-=1

nums1=[1,2,3,0,0,0]
nums2=[2,5,6]
merge2(nums1,3,nums2,3)
print(nums1)