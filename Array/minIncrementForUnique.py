'''
Source : https://leetcode.com/problems/minimum-increment-to-make-array-unique/description/
Author : Yuan Wang
Date   : 2019-01-10

/********************************************************************************** 
*Given an array of integers A, a move consists of choosing any A[i], and incrementing
*it by 1.
*
*Return the least number of moves to make every value in A unique.
*
*Example 1:
*
*
*Input: [1,2,2]
*Output: 1
*Explanation:  After 1 move, the array could be [1, 2, 3].
*Example 2:
*
*Input: [3,2,1,2,1,7]
*Output: 6
*Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
*It can be shown with 5 or less moves that it is impossible for the array to have 
*all unique 
**********************************************************************************/
'''

import collections

#Other solution, Time complexity:O(N)
def minIncrementForUnique(A):
    count = collections.Counter(A)
    taken = []

    ans = 0
    for x in range(100000):
        if count[x] >= 2:
            taken.extend([x] * (count[x] - 1))
        elif taken and count[x] == 0:
            ans += x - taken.pop()
    return ans

import unittest
class Test(unittest.TestCase):

    def setUp(self):
        self.A = [1,2,2]
        self.B = [3,2,1,2,1,7]

    def test(self):
        self.assertEqual(minIncrementForUnique(self.A),1)
        self.assertEqual(minIncrementForUnique(self.B),6)


if __name__ == '__main__':
    unittest.main()
