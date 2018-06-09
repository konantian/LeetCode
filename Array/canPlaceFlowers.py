'''
Source : https://leetcode.com/problems/can-place-flowers/
Author : Yuan Wang
Date   : 2018-06-09

Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2

Time complexity:O(n), Space complexity:O(1)
'''

#Greedy to place a flower from left to right as many as possible
#for an empty position, if the left and right of it are both empty means
#this place can be planted a flower
def canPlaceFlowers(flowerbed, n):
	"""
	:type flowerbed: List[int]
	:type n: int
	:rtype: bool
	"""
	count=0
	flowerbed[:]=[0]+flowerbed+[0]
	for i in range(1,len(flowerbed)-1):
		if flowerbed[i]==0:
			if flowerbed[i-1] == 0 and flowerbed[i+1]==0:
				flowerbed[i]=1
				count+=1
	
	return count >= n

flowerbed=[0,0,0,1,0,0,0,0,0,1,0,1]
n=4
print(canPlaceFlowers(flowerbed,n))