'''
Source : https://leetcode.com/problems/fair-candy-swap/
Author : Yuan Wang
Date   : 2019-01-01

/********************************************************************************** 
*Alice and Bob have candy bars of different sizes: A[i] is the size of the i-th bar
*of candy that Alice has, and B[j] is the size of the j-th bar of candy that Bob has.
*
*Since they are friends, they would like to exchange one candy bar each so that after
*the exchange, they both have the same total amount of candy.  (The total amount of
*candy a person has is the sum of the sizes of candy bars they have.)
*
*Return an integer array ans where ans[0] is the size of the candy bar that Alice must
*exchange, and ans[1] is the size of the candy bar that Bob must exchange.

Example 1:

Input: A = [1,1], B = [2,2]
Output: [1,2]
Example 2:

Input: A = [1,2], B = [2,3]
Output: [1,2]
Example 3:

Input: A = [2], B = [1,3]
Output: [2,3]
Example 4:

Input: A = [1,2,5], B = [2,4]
Output: [5,4]
**********************************************************************************/
'''
import unittest

#Time complexity:O(n) Space complexity:O(1)
def fairCandySwap(A, B):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: List[int]
    """
        
    sumA = sum(A)
    sumB = sum(B)
    setB = set(B)
        
    candidate = int((sumB-sumA)/2)
        
    for x in A:
        if x + candidate in setB:
            return [x,x+candidate]



class Test(unittest.TestCase):

    def setUp(self):
        self.A = [1,2,5]
        self.B = [2,4]

    def test_A(self):
        self.assertEqual(fairCandySwap(self.A,self.B), [5,4])

    def test_B(self):
        self.assertEqual(fairCandySwap([2],[1,3]),[2,3])

if __name__ == '__main__':
    unittest.main()