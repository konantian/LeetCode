'''
Source : https://leetcode.com/problems/counting-bits/
Author : Yuan Wang
Date   : 2021-01-24

/*************************************************************************************** 
*Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num 
*calculate the number of 1's in their binary representation and return them as an array.
*
*
*Example:
*Input: 2
*Output: [0,1,1]
*Input: 5
*Output: [0,1,1,2,1,2]
****************************************************************************************/
 '''
 
 #Bit manipulation and DP, time complexity : O(n), space complexity : (n)
 def countBits(self, num: int) -> List[int]:
    result = [0,1]
    if num <= 1:
        return result[:num+1]
    for i in range(2, num + 1):
        value = result[i>>1]
        if i % 2 == 0:
            result.append(value)
        else:
            result.append(value+1)
    return result