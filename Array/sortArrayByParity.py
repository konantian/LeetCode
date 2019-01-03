'''
Source : https://leetcode.com/problems/sort-array-by-parity/
Author : Yuan Wang
Date   : 2019-01-02

/********************************************************************************** 
*Given an array A of non-negative integers, return an array consisting of all the 
*even elements of A, followed by all the odd elements of A.
*
*You may return any answer array that satisfies this condition.
Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
**********************************************************************************/
'''

#Time complexity:O(n) Space complexity:O(n)
def sortArrayByParity(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    return [i for i in A if i % 2 == 0] + [i for i in A if i % 2 != 0]



import unittest
class Test(unittest.TestCase):

    def setUp(self):
        self.A = [3,1,2,4]

    def test_A(self):
        self.assertEqual(sortArrayByParity(self.A), [2,4,3,1])

if __name__ == '__main__':
    unittest.main()
