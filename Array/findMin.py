'''
Source : https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
Author : Yuan Wang
Date   : 2021-01-21

/*************************************************************************************** 
*Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
*For example, the array nums = [0,1,2,4,5,6,7] might become:

*Example 1:
*Input: nums = [3,4,5,1,2]
*Output: 1

 ****************************************************************************************
 '''
 
 #self solution, time complexity : O(N), space complexity : O (1)
 def findMin(self, nums: List[int]) -> int:
    p = 0
    q = len(nums) - 1
    while p <= q:
        if nums[p] < nums[q]:
            return nums[p]
        else:
            p += 1
    return nums[q]

#Binary search solution, time complexity : O(logn), space complexity : O(1)
def findMin(self, nums: List[int]) -> int:
 
    if not nums or len(nums) == 0:
        return 0
    
    if nums[0] < nums[-1]:
        return nums[0]
    
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[right]:
            right = mid
        else:
            left = mid + 1
    
    return nums[left]