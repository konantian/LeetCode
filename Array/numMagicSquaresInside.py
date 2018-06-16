'''
Source : https://leetcode.com/problems/magic-squares-in-grid/
Author : Yuan Wang
Date   : 2018-06-16

/********************************************************************************** 
*A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such 
*that each row, column, and both diagonals all have the same sum.
*
*Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  
*(Each subgrid is contiguous).
*
*Example 1:
*
*Input: [[4,3,8,4],
*	[9,5,1,9],
*	[2,7,6,2]]
*Output: 1
*Explanation: 
*The following subgrid is a 3 x 3 magic square:
*438
*951
*276
*
*while this one is not:
*384
*519
*762
*
*In total, there is only one magic square inside the given grid.
**********************************************************************************/
'''

def check_sum(matrix):
	for i in range(3):
		total=0
		for j in range(3):
			total+=matrix[i][j]
		if total != 15:
			return False
	if matrix[0][0]+matrix[1][1]+matrix[2][2] != 15:
		return False
	if matrix[0][2]+matrix[1][1]+matrix[2][0] != 15:
		return False
	return True
	
def check_number(numbers):
	d={1:False,2:False,3:False,4:False,5:False,6:False,7:False,8:False,9:False}
	for i in numbers:
		if i in d:
			if d[i]==False:
				d[i]=True
			elif d[i] == True:
				return False
			else:
				return False
	return True
def numMagicSquaresInside(grid):
	"""
	:type grid: List[List[int]]
	:rtype: int
	"""
	count=0
	for i in range(0,len(grid)-2):
		for j in range(0,len(grid[0])-2):
			numbers=[grid[i][j],grid[i][j+1],grid[i][j+2],grid[i+1][j],grid[i+1][j+1],grid[i+1][j+2],grid[i+2][j],grid[i+2][j+1],grid[i+2][j+2]]
			if check_number(numbers) == True:
				matrix=[[grid[i][j],grid[i][j+1],grid[i][j+2]],[grid[i+1][j],grid[i+1][j+1],grid[i+1][j+2]],[grid[i+2][j],grid[i+2][j+1],grid[i+2][j+2]]]
				if check_sum(matrix) == True:
					count+=1
	return count
def numMagicSquaresInsideB(grid):
	R, C = len(grid), len(grid[0])

	def magic(a,b,c,d,e,f,g,h,i):
		return (sorted([a,b,c,d,e,f,g,h,i]) == range(1, 10) and
			(a+b+c == d+e+f == g+h+i == a+d+g ==
	 		b+e+h == c+f+i == a+e+i == c+e+g == 15))

	ans = 0
	for r in range(R-2):
		for c in range(C-2):
			if magic(grid[r][c], grid[r][c+1], grid[r][c+2],
	 			grid[r+1][c], grid[r+1][c+1], grid[r+1][c+2],
	 			grid[r+2][c], grid[r+2][c+1], grid[r+2][c+2]):
				ans += 1
	return ans

grid=[[5,4,7,8,5,4,6,8,2,9],[5,3,6,8,1,5,1,1,8,5],[8,9,6,8,4,7,3,4,9,1],[9,3,8,9,2,8,3,8,7,1],[1,1,1,7,3,3,9,1,8,7],[1,5,5,7,1,6,7,9,3,4],[2,3,3,8,8,1,1,6,5,7],[7,8,5,4,7,9,4,6,5,3],[8,5,2,7,1,3,7,2,8,9],[4,9,4,3,9,4,5,4,7,1]]
print(numMagicSquaresInsideB(grid))