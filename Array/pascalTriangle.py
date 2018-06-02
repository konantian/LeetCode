'''
Source : https://oj.leetcode.com/problems/pascals-triangle/
Author : Yuan Wang
Date   : 2018-06-01

/********************************************************************************** 
* 
* Given numRows, generate the first numRows of Pascal's triangle.
* 
* For example, given numRows = 5,
* Return
* 
* [
*	  [1],
*	 [1,1],
*	[1,2,1],
*   [1,3,3,1],
*  [1,4,6,4,1]
* ]
* 
*	   
**********************************************************************************/
'''
def generate(numRows):
	"""
	:type numRows: int
	:rtype: List[List[int]]
	"""
	
	LL = [[1]]
	if numRows == 0:
		return []
	for i in range(1,numRows):
		LL.append([(0 if j== 0 else LL[i-1][j-1])+ (0 if j ==len(LL[i-1]) else LL[i-1][j]) for j in range(i+1)])
	return LL

#	1 3 3 1 0 
# +  0 1 3 3 1
# =  1 4 6 4 1
def generate(numRows):
	LL=[]
	if numRows == 0:
		return LL
	elif numRows == 1:
		return [[1]]
	row=[1]
	LL.append(row)
	for _ in range(numRows-1):
		row = [x + y for x, y in zip([0]+row, row+[0])]
		LL.append(row)
	return LL