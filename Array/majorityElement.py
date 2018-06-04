'''
Source : https://oj.leetcode.com/problems/majority-element/
Author : Yuan Wang
Date   : 2018-06-04

/********************************************************************************** 
 * 
 * Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
 * 
 * You may assume that the array is non-empty and the majority element always exist in the array.
 * 
 * Credits:Special thanks to @ts for adding this problem and creating all test cases.
 *   
 **********************************************************************************/
 '''
import collections

#self solution, slowly
def majorityElementA(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n=len(nums)
    dic={}
    if n == 1:
        return nums[0]
    for i in nums:
        if i in dic:
            dic[i] +=1
            if dic[i] > int((n/2)):
                return i
        else:
            dic[i]=1
#Boyer-Moore Voting Algorithm
def majorityElementB(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    candidate = None
    
    for i in nums:
        if count == 0:
            candidate = i
        count += (1 if i == candidate else -1)
    return candidate

'''
after sorted, the majority element must appear at the middle of the list,since it has
at least (n/2)+1 elements
For this algorithm, we simply do exactly what is described: sort nums, and return the
element in question. To see why this will always return the majority element (given 
that the array has one), consider the figure below (the top example is for an odd-length 
array and the bottom is for an even-length array)
Complexity Analysis

Time complexity : O(nlgn)

Sorting the array costs O(nlgn) time in Python and Java, so it dominates the overall runtime.

Space complexity : O(1) or O(n)

We sorted nums in place here - if that is not allowed, then we must spend linear additional space on a copy of nums and sort the copy instead.
'''
def majorityElementC(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    a = sorted(nums)
    return a[int(len(a)/2)]


'''
using Counter to count the appear times for each element
and return the one who has the most appear times
Complexity Analysis

Time complexity : O(n)

We iterate over nums once and make a constant time HashMap insertion on each iteration. 
Therefore, the algorithm runs in O(n) time.

Space complexity : O(n)

'''
def majorityElementD(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    counts = collections.Counter(nums)
    return max(counts.keys(), key=counts.get)

print(majorityElementA([1]))
