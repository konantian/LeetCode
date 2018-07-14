'''
Source : https://leetcode.com/problems/jewels-and-stones/
Author : Yuan Wang
Date   : 2018-07-14

/*************************************************************************************** 
*You're given strings J representing the types of stones that are jewels, and S representing
*the stones you have.  Each character in S is a type of stone you have.  You want to know 
*how many of the stones you have are also jewels.
*
*The letters in J are guaranteed distinct, and all characters in J and S are letters. 
*Letters are case sensitive, so "a" is considered a different type of stone from "A".
*
*Example 1:
*
*Input: J = "aA", S = "aAAbbbb"
*Output: 3
*Example 2:
*
*Input: J = "z", S = "ZZ"
*Output: 0	   
****************************************************************************************/
 '''

import collections

#Time complexity:O(n) Space complexity:O(1)
 def numJewelsInStones(J, S):
	"""
	:type J: str
	:type S: str
	:rtype: int
	"""
	dic=collections.Counter(S)
	count=0
	for i in J:
		if i in dic:
			count+=dic[i]
	
	return count

J="aA"
S="aAAbbbb"
print(numJewelsInStones(J,S))