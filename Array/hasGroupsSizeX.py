'''
Source : https://leetcode.com/problems/groups-of-special-equivalent-strings/
Author : Yuan Wang
Date   : 2019-01-09

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

#Self solution, Brute Force, Time complexity:O(N^2loglogN)
from collections import Counter

def hasGroupsSizeX(deck):
    """
    :type deck: List[int]
    :rtype: bool
    """
    if len(deck) < 2:
        return False
    d=Counter(deck)
    test=max(d.values())
    for i in range(2,test+1):
        result=sum([d[count] % i for count in d])
        if result == 0:
            return True
    return False


#Other solution, using GCD, time complexity:O(Nlog^2N)
def hasGroupsSizeXB(deck):
    """
    :type deck: List[int]
    :rtype: bool
    """
    from math import gcd
    from functools import reduce

    vals = Counter(deck).values()
    return reduce(gcd, vals) >= 2


import unittest
class Test(unittest.TestCase):

    def setUp(self):
        self.A = [1,2,3,4,4,3,2,1]
        self.B = [1,1,1,2,2,2,3,3]

    def testA(self):
        self.assertEqual(hasGroupsSizeX(self.A),True)

    def testB(self):
        self.assertEqual(hasGroupsSizeXB(self.B),False)



if __name__ == '__main__':
    unittest.main()