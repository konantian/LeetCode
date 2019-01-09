'''
Source : https://leetcode.com/problems/groups-of-special-equivalent-strings/
Author : Yuan Wang
Date   : 2019-01-08

/********************************************************************************** 
*You are given an array A of strings.
*
*Two strings S and T are special-equivalent if after any number of moves, S == T.
*
*A move consists of choosing two indices i and j with i % 2 == j % 2, and swapping 
*S[i] with S[j].
*
*Now, a group of special-equivalent strings from A is a non-empty subset S of A such
*that any string not in S is not special-equivalent with any string in S.
*
*Return the number of groups of special-equivalent strings from A.

Example 1:

Input: ["a","b","c","a","c","c"]
Output: 3
Explanation: 3 groups ["a","a"], ["b"], ["c","c","c"]
Example 2:

Input: ["aa","bb","ab","ba"]
Output: 4
Explanation: 4 groups ["aa"], ["bb"], ["ab"], ["ba"]
**********************************************************************************/
'''


def numSpecialEquivGroups(A):
    """
    :type A: List[str]
    :rtype: int
    """
    def count(A):
        ans = [0] * 52
        for i, letter in enumerate(A):
            ans[ord(letter) - ord('a') + 26 * (i%2)] += 1
        return tuple(ans)

    return len({count(word) for word in A})


import unittest
class Test(unittest.TestCase):

    def setUp(self):
        self.A = ["a","b","c","a","c","c"]
        self.B = ["aa","bb","ab","ba"]

    def test(self):
        self.assertEqual(numSpecialEquivGroups(self.A),3)
        self.assertEqual(numSpecialEquivGroups(self.B),4)


if __name__ == '__main__':
    unittest.main()