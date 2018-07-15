'''
Source : https://leetcode.com/problems/transpose-matrix/
Author : Yuan Wang
Date   : 2018-07-15

/*************************************************************************************** 
*Given a matrix A, return the transpose of A.
*
*The transpose of a matrix is the matrix flipped over it's main diagonal, switching the 
*row and column indices of the matrix.
*
*
*
*Example 1:
*
*Input: [[1,2,3],[4,5,6],[7,8,9]]
*Output: [[1,4,7],[2,5,8],[3,6,9]]
*Example 2:
*
*Input: [[1,2,3],[4,5,6]]
*Output: [[1,4],[2,5],[3,6]] 
****************************************************************************************/
 '''

 #Self solution, Time complexity:O(n) Space complexity:O(n)
 def transpose(A):
	"""
	:type A: List[List[int]]
	:rtype: List[List[int]]
	"""
	result=[]
	for i in range(len(A[0])):
		temp=[]
		for j in range(len(A)):
			temp+=[A[j][i]]
	
		result.append(temp)
	
	return result

#Pythonic solution
def transposeB(A):
	"""
	:type A: List[List[int]]
	:rtype: List[List[int]]
	"""

	return list(zip(*A))


def transposeC(A):
	"""
	:type A: List[List[int]]
	:rtype: List[List[int]]
	"""
	
	
	result = [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]
	return (result)
	
A=[[1,2,3],[4,5,6],[7,8,9]]
print(transpose(A))