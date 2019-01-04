'''
Source : https://leetcode.com/problems/reverse-only-letters/
Author : Yuan Wang
Date   : 2019-01-04

/********************************************************************************** 
*Given a string S, return the "reversed" string where all characters that are not a 
*letter stay in the same place, and all letters reverse their positions.
* 
*Example 1:
*
*Input: "ab-cd"
*Output: "dc-ba"
*Example 2:
*
*Input: "a-bC-dEf-ghIj"
*Output: "j-Ih-gfE-dCba"
*Example 3:
*
*Input: "Test1ng-Leet=code-Q!"
*Output: "Qedo1ct-eeLg=ntse-T!"
**********************************************************************************/
'''

#Self solution, Time complexity:O(n) Space complexity:O(n)
def reverseOnlyLettersA(S):
    """
    :type S: str
    :rtype: str
    """
    S=list(S)
    i=0
    j=len(S)-1
    while i < j:
        if S[i].isalpha() and S[j].isalpha():
            S[i],S[j]=S[j],S[i]
            i+=1
            j-=1
        elif S[i].isalpha() and not S[j].isalpha():
            j-=1
        elif not S[i].isalpha() and S[j].isalpha():
            i+=1
        else:
            i+=1
            j-=1
    S="".join(S)
    return S

#Other solution,Time complexity:O(n) Space complexity:O(n)
def reverseOnlyLettersB(S):
    letters = [c for c in S if c.isalpha()]
    ans = []
    for c in S:
        if c.isalpha():
            ans.append(letters.pop())
        else:
            ans.append(c)
    return "".join(ans)

import unittest
class Test(unittest.TestCase):

    def setUp(self):
        self.A = "Test1ng-Leet=code-Q!"
        self.B = "73-]"

    def test_A(self):
        self.assertEqual(reverseOnlyLettersA(self.A), "Qedo1ct-eeLg=ntse-T!")
        self.assertEqual(reverseOnlyLettersA(self.B), "73-]")

    def test_B(self):
    	self.assertEqual(reverseOnlyLettersB(self.A), "Qedo1ct-eeLg=ntse-T!")
    	self.assertEqual(reverseOnlyLettersB(self.B), "73-]")

if __name__ == '__main__':
    unittest.main()