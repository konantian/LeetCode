'''
Source : https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/
Author : Yuan Wang
Date   : 2019-05-18

/*************************************************************************************** 
Given a binary string S (a string consisting only of '0' and '1's) and a positive integer
 N, return true if and only if for every integer X from 1 to N, the binary representation
 of X is a substring of S.

 

Example 1:

Input: S = "0110", N = 3
Output: true
Example 2:

Input: S = "0110", N = 4
Output: false
****************************************************************************************/
 '''
#Self solution
def queryString(S: str, N: int) -> bool:
    for i in range(1,N+1):
        if bin(i)[2:] not in S:
            return False
    return True