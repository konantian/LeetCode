'''
Source : https://leetcode.com/problems/squares-of-a-sorted-array/
Author : Yuan Wang
Date   : 2019-03-02

/********************************************************************************** 
Given an array of integers A sorted in non-decreasing order, return an array of the
squares of each number, also in sorted non-decreasing order.

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
**********************************************************************************/
'''

#Self Pythonic solution
def sortedSquares(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """

    return sorted([i*i for i in A])

#Solution with two pointer
def sortedSquares(A):
	answer = [0] * len(A)
	l, r = 0, len(A) - 1
	while l <= r:
		left, right = abs(A[l]), abs(A[r])
		if left > right:
			answer[r - l] = left * left
			l += 1
		else:
			answer[r - l] = right * right
			r -= 1
	return answer

#Self solution using stack and list reverse
def sortedSquares(A):
    answer = []
    l, r = 0, len(A) - 1
    while l <= r:
        left, right = abs(A[l]), abs(A[r])
        if left > right:
            answer.append(left * left)
            l += 1
        else:
            answer.append(right * right)
            r -= 1
            
    return answer[::-1]


