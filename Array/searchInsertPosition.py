'''
Source : https://oj.leetcode.com/problems/search-insert-position/
Author : Yuan Wang
Date   : 2018-05-27

**********************************************************************************
 *
 * Given a sorted array and a target value, return the index if the target is found.
 * If not, return the index where it would be if it were inserted in order.
 *
 * You may assume no duplicates in the array.
 *
 * Here are few examples.
 * [1,3,5,6], 5 → 2
 * [1,3,5,6], 2 → 1
 * [1,3,5,6], 7 → 4
 * [1,3,5,6], 0 → 0
 *
 *
 **********************************************************************************/
 '''
#52 ms
def searchInsertA(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if target in nums:
        return nums.index(target)
    else:
        if len(nums) > 1:
            for i in range(len(nums)-1):
                if target > nums[i] and target < nums[i+1]:
                    return i+1
                else:
                    if target > nums[-1]:
                        return len(nums)
                    elif target < nums[0]:
                        return 0
        else:
            if target > nums[0]:
                return 1
            else:
                return 0

#48 ms, using binary search to find the position，O(logn)
def searchInsertB(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums)-1
        while high>=low:
            middle = (low+high) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                low=middle+1
            else:
                high=middle-1
        return low

#36 ms,i is the index, num is the element in list,O(n) in worst 
def searchInsertC(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i, num in enumerate(nums):
            print(i,num)
            if num >= target:
                return i
        return len(nums)

#40ms,O(n) in worst
def searchInsertD(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l=len(nums)
        for i in range(l):
            if (nums[i]>=target):
                return i
        return l
#36ms, O(n) in worst 
def searchInsertE(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        num=[i for i in nums if i<target]
        return len(num)

array=[1,3,5,6]
print(searchInsertE(array,2))