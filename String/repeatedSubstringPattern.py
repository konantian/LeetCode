
#Source : https://leetcode.com/problems/repeated-substring-pattern/
#Author : Yuan Wang
#Date   : 2018-07-03
'''
********************************************************************************** 
*Given a non-empty string check if it can be constructed by taking a substring of it
*and appending multiple copies of the substring together. You may assume the given 
*string consists of lowercase English letters only and its length will not exceed 10000.
*Example 1:
*Input: "abab"
*
*Output: True
*
*Explanation: It's the substring "ab" twice.
*Example 2:
*Input: "aba"
*
*Output: False
*Example 3:
*Input: "abcabcabcabc"
*
*Output: True
*
*Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
**********************************************************************************/
'''

#Self solution
def repeatedSubstringPatternA(s):
    """
    :type s: str
    :rtype: bool
    """
    if not s or len(s) == 1:
        return False
    
    if s[:len(s)//2]==s[len(s)//2:]:
        return True

    for i in range(1,len(s)//2+1):
        if s[i] == s[0]:
            substring=s[:i]
            if substring*(len(s)//len(substring))==s:
                return True
    return False

'''
Pythonic solution, if the string is repeated, then s must in (s+s)[1:-1]
Time complexity:O(n) Space complexity:O(1)
Basic idea:

First char of input string is first char of repeated substring
Last char of input string is last char of repeated substring
Let S1 = S + S (where S in input string)
Remove 1 and last char of S1. Let this be S2
If S exists in S2 then return true else false
Let i be index in S2 where S starts then repeated substring 
length i + 1 and repeated substring S[0: i+1] 
'''
def repeatedSubstringPatternB(s):
    """
    :type s: str
    :rtype: bool
    """
    return s in (s + s)[1:-1]

s="abcabcabc"
print(repeatedSubstringPatternA(s))