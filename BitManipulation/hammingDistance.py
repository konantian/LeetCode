'''
Source : https://leetcode.com/problems/hamming-distance/
Author : Yuan Wang
Date   : 2021-01-26

/*************************************************************************************** 
*The Hamming distance between two integers is the number of positions at which the 
*corresponding bits are different.
*
*Given two integers x and y, calculate the Hamming distance.
****************************************************************************************/
 '''
 
def hammingDistance(self, x: int, y: int) -> int:
    counter = 0 
    while x != 0 or y != 0:
        if (x % 2) != (y % 2):
            counter += 1
        x = x >> 1
        y = y >> 1
    return counter