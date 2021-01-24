'''
Source : https://leetcode.com/problems/number-of-1-bits/
Author : Yuan Wang
Date   : 2021-01-24

/*************************************************************************************** 
*Write a function that takes an unsigned integer and returns the number of '1' bits it 
*has (also known as the Hamming weight).
*
*Example:
*Input: n = 00000000000000000000000000001011
*Output: 3
****************************************************************************************/
 '''
 
 #Bit manipulation, time complexity : O(n), space complexity : O(1)
 def hammingWeight(self, n: int) -> int:
    total = 0
    while n != 0:
        total += 1
        n &= (n - 1)
    return total