'''
Source : https://leetcode.com/problems/ugly-number/
Author : Yuan Wang
Date   : 2019-01-04

/********************************************************************************** 
*Write a program to check whether a given number is an ugly number.
*
*Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
*
*Example 1:
*
*Input: 6
*Output: true
*Explanation: 6 = 2 × 3
*Example 2:
*
*Input: 8
*Output: true
*Explanation: 8 = 2 × 2 × 2
*Example 3:
*
*Input: 14
*Output: false 
*Explanation: 14 is not ugly since it includes another prime factor 7.
**********************************************************************************/
'''

def isUgly(num):
    """
    :type num: int
    :rtype: bool
    """
    if num <= 0:
        return False
    for p in 2, 3, 5:
        while num % p == 0:
            num /= p
    return num == 1



import unittest
class Test(unittest.TestCase):

    def setUp(self):
        self.A = 6
        self.B = 8
        self.C = 14

    def test(self):
        self.assertEqual(isUgly(self.A), True)
        self.assertEqual(isUgly(self.B), True)
        self.assertEqual(isUgly(self.C), False)


if __name__ == '__main__':
    unittest.main()