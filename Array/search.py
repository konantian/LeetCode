'''
Source : https://leetcode.com/problems/search-in-rotated-sorted-array/
Author : Yuan Wang
Date   : 2021-01-21

/********************************************************************************** 
* 
* You are given an integer array nums sorted in ascending order (with distinct values), and an integer target.
*
*Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
*
*If target is found in the array return its index, otherwise, return -1.
* 
*Example 1:
* 
* Input: nums = [4,5,6,7,0,1,2], target = 0
* Output: 4
*	   
**********************************************************************************/
'''
def search(self, nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    
    while l <= r:
        mid = (l + r) // 2
        if target == nums[mid]:
            return mid
        # nums[left to mid] is sorted 
        if nums[l] <= nums[mid]:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        # nums[mid to right] is sorted
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1
    return -1