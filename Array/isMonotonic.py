'''
Source : https://leetcode.com/problems/monotonic-array/
Author : Yuan Wang
Date   : 2019-01-01

/********************************************************************************** 
*An array is monotonic if it is either monotone increasing or monotone decreasing.
*
*An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A 
*is monotone decreasing if for all i <= j, A[i] >= A[j].
*
*Return true if and only if the given array A is monotonic.

Example 1:

Input: [1,2,2,3]
Output: true
Example 2:

Input: [6,5,4,4]
Output: true
Example 3:

Input: [1,3,2]
Output: false
Example 4:

Input: [1,2,4,5]
Output: true
Example 5:

Input: [1,1,1]
Output: true
**********************************************************************************/
'''

#Time complexity O(n), Space complexity:O(1)
def isMonotonic(A):
    """
    :type A: List[int]
    :rtype: bool
    """
        
    mode = None
    for i in range(1,len(A)):
        if A[i] > A[i-1]:
            if mode == None:
                mode = "Inc"
            else:
                if mode != "Inc":
                    return False
        elif A[i] < A[i-1]:
            if mode == None:
                mode = "Dec"
            else:
                if mode != "Dec":
                    return False
                    
    return True

import unittest
class Test(unittest.TestCase):

    def setUp(self):
    	self.caseA = [1,2,2,3]
    	self.caseB = [6,5,4,4]
    	self.caseC = [1,3,2]


    def test(self):
        self.assertEqual(isMonotonic(self.caseA), True)
        self.assertEqual(isMonotonic(self.caseB), True)
        self.assertEqual(isMonotonic(self.caseC), False)


if __name__ == '__main__':
    unittest.main()