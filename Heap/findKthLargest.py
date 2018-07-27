#Source : https://leetcode.com/problems/kth-largest-element-in-an-array/
#Author : Yuan Wang
#Date   : 2018-07-27
'''
********************************************************************************** 
*Find the kth largest element in an unsorted array. Note that it is the kth largest
*element in the sorted order, not the kth distinct element.
*
*Example 1:
*
*Input: [3,2,1,5,6,4] and k = 2
*Output: 5
*Example 2:
*
*Input: [3,2,3,1,2,4,5,5,6] and k = 4
*Output: 4
**********************************************************************************/
'''

import heapq
#Self solution using heap, Time complexity:O(k+(n-k)lgk)
def findKthLargestA(nums, k):
	"""
	:type nums: List[int]
	:type k: int
	:rtype: int
	"""
	
	heapq.heapify(nums)
	
	return heapq.nlargest(k,nums)[-1]

#Self solution using quick select,Time complexity:O(n)
def findKthLargestB(nums, k):
	"""
	:type nums: List[int]
	:type k: int
	:rtype: int
	"""
	return select(nums,len(nums)-k)
	
def partition(x,pivot=0):
	i=0
	if pivot != 0:
		x[0],x[pivot]=x[pivot],x[0]
	for j in range(len(x)-1):
		if x[j+1]<x[0]:
			x[j+1],x[i+1]=x[i+1],x[j+1]
			i+=1
	x[0],x[i]=x[i],x[0]
	return x,i
	
def select(nums,k):
	if nums:
		xpart=partition(nums,random.randrange(len(nums)))
		x=xpart[0]
		j=xpart[1]
		if j == k:
			return x[j]
		elif j > k:
			return select(x[:j],k)
		else:
			k=k-j-1
			return select(x[(j+1):],k)

#Other solution using heapq
def findKthLargestC(nums, k):
	"""
	:type nums: List[int]
	:type k: int
	:rtype: int
	"""
	heap = nums[:k]
	heapq.heapify(heap)
	for n in nums[k:]:
		heapq.heappushpop(heap, n)
	return heap[0]

