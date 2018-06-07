'''
Source : https://leetcode.com/problems/third-maximum-number/
Author : Yuan Wang
Date   : 2018-06-07

/*************************************************************************************** 
 *
 * Given a non-empty array of integers, return the third maximum number in this array. 
 * If it does not exist, return the maximum number. The time complexity must be in O(n).
 * 
 * Example 1:
 * 
 * Input: [3, 2, 1]
 * 
 * Output: 1
 * 
 * Explanation: The third maximum is 1.
 * 
 * Example 2:
 * 
 * Input: [1, 2]
 * 
 * Output: 2
 * 
 * Explanation: The third maximum does not exist, so the maximum (2) is returned 
 * instead.
 * 
 * Example 3:
 * 
 * Input: [2, 2, 3, 1]
 * 
 * Output: 1
 * 
 * Explanation: Note that the third maximum here means the third maximum distinct 
 * number.
 * Both numbers with value 2 are both considered as second maximum.
 ***************************************************************************************/
 '''

from random import *

def thirdMax(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    nums=list(set(nums))
    if len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return max(nums)
    return select(nums,len(nums)-3)

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
    xpart=partition(nums,randrange(len(nums)))
    x=xpart[0]
    j=xpart[1]
    if j == k:
        return x[j]
    elif j > k:
        return select(x[:j],k)
    else:
        k=k-j-1
        return select(x[(j+1):],k)

def thirdMaxB(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    nums=sorted(list(set(nums)))
    if len(nums) < 3:
        return nums[-1]
    return nums[-3]

print(thirdMaxB([2,2,3,1]))
    