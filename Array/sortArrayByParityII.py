'''
Source : https://leetcode.com/problems/sort-array-by-parity/
Author : Yuan Wang
Date   : 2019-01-03

/********************************************************************************** 
*Given an array A of non-negative integers, half of the integers in A are odd, and 
*half of the integers are even.
*
*Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
*
*You may return any answer array that satisfies this condition.

Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5]
would be accepted
**********************************************************************************/
'''

#Self solution, Time complexity:O(n) Space complexity:O(n)
def sortArrayByParityII(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    B=[0]*len(A)
        
    even = 0
    odd = 1
    for i in A:
        if i % 2 == 0:
            B[even] = i
            even += 2
        else:
            B[odd] = i
            odd += 2
    return B

import unittest
class Test(unittest.TestCase):

    def setUp(self):
        self.A = [4,2,5,7]

    def test_A(self):
        self.assertEqual(sortArrayByParityII(self.A), [4,5,2,7])

if __name__ == '__main__':
    unittest.main()