'''
Source : https://leetcode.com/problems/max-consecutive-ones/
Author : Yuan Wang
Date   : 2018-06-08

Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
Time complexity:O(n),Space complexity:O(1)
'''
def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        amount=0
        for i in nums:
            if i == 1:
                count+=1
            else:
                count=0
            amount = count if amount < count else amount 
            #compare two elements using "<" is faster than max()
        return amount