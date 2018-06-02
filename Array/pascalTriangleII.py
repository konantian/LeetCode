'''
Source : https://oj.leetcode.com/problems/pascals-triangle-ii/
Author : Yuan Wang
Date   : 2018-06-02

/********************************************************************************** 
* 
* Given an index k, return the kth row of the Pascal's triangle.
* 
* For example, given k = 3,
* Return [1,3,3,1].
* 
* Note:
* Could you optimize your algorithm to use only O(k) extra space?
* 
*	   
********************************************************************************
'''
import math
def getRow(rowIndex):
	"""
	:type rowIndex: int
	:rtype: List[int]
	"""
	row = [1]
	for _ in range(rowIndex):
		row = [x + y for x, y in zip([0]+row, row+[0])]
	return row
print(getRow(3))