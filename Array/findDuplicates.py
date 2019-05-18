'''
Source : https://leetcode.com/problems/find-all-duplicates-in-an-array/
Author : Yuan Wang
Date   : 2019-05-17

/*************************************************************************************** 
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
  
****************************************************************************************/
 '''
 #Self solution,Time complexity:O(n) Space complexity:O(n)
 def findDuplicates(nums: List[int]) -> List[int]:
    result = set([])
    final = []
    for num in nums:
        if num not in result:
            result.add(num)
        else:
            final.append(num)
    return final


#Other solutin, Space complexity:O(1)
#The idea is we do a linear pass using the input array itself as a hash to store which 
#numbers have been seen before. We do this by making elements at certain indexes negative.
def findDuplicates(nums: List[int]) -> List[int]:
    result = []
    for num in nums:
        if nums[abs(num)-1] < 0:
            result.append(abs(num))
        else:
            nums[abs(num)-1] *= -1
    return result