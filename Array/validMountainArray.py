'''
Source : https://leetcode.com/problems/valid-mountain-array/
Author : Yuan Wang
Date   : 2019-01-07

/********************************************************************************** 
*Given an array A of integers, return true if and only if it is a valid mountain array.
*
*Recall that A is a mountain array if and only if:
*
*A.length >= 3
*There exists some i with 0 < i < A.length - 1 such that:
*A[0] < A[1] < ... A[i-1] < A[i]
*A[i] > A[i+1] > ... > A[B.length - 1]

Example 1:

Input: [2,1]
Output: false
Example 2:

Input: [3,5,5]
Output: false
**********************************************************************************/
'''

def validMountainArray(A):
    """
    :type A: List[int]
    :rtype: bool
    """
    N = len(A)
    i = 0

    # walk up
    while i+1 < N and A[i] < A[i+1]:
        i += 1

    # peak can't be first or last
    if i == 0 or i == N-1:
        return False

    # walk down
    while i+1 < N and A[i] > A[i+1]:
        i += 1

    return i == N-1



import unittest
class Test(unittest.TestCase):

    def setUp(self):
        self.A = [2,1]
        self.B = [0,3,2,1]

    def test(self):
        self.assertEqual(validMountainArray(self.A), False)
        self.assertEqual(validMountainArray(self.B), True)


if __name__ == '__main__':
    unittest.main()