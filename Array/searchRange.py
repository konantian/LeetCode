'''
Source : https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
Author : Yuan Wang
Date   : 2021-01-011

/********************************************************************************** 
*Given an array of integers nums sorted in ascending order, find the starting and 
*ending position of a given target value.

If target is not found in the array, return [-1, -1].
*
Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1, -1]
**********************************************************************************/
'''

#Linear search solution, Time complexity : O(n), Space complexity : O(1)
def searchRange(nums: List[int], target: int) -> List[int]:
    result = []
    for index, num in enumerate(nums):
        if num == target:
            result.append(index)
            
    if not result: return [-1,-1]
    return [result[0],result[-1]]

#Binary search solution, Time complexity : O(logn), Space complexity : O(1)
def searchRange(nums: List[int], target: int) -> List[int]:
    left_idx = searchRangeHelper(nums, target, True)

    # assert that `left_idx` is within the array bounds and that `target`
    # is actually in `nums`.
    if left_idx == len(nums) or nums[left_idx] != target:
        return [-1, -1]

    return [left_idx, searchRangeHelper(nums, target, False)-1]

def searchRangeHelper(nums, target, left):
    lo = 0
    hi = len(nums)

    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > target or (left and target == nums[mid]):
            hi = mid
        else:
            lo = mid+1

    return lo