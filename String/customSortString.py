'''
Source : https://leetcode.com/problems/custom-sort-string/
Author : Yuan Wang
Date   : 2019-05-18

/*************************************************************************************** 
S and T are strings composed of lowercase letters. In S, no letter occurs more than once.

S was sorted in some custom order previously. We want to permute the characters of T so 
that they match the order that S was sorted. More specifically, if x occurs before y in S,
then x should occur before y in the returned string.

Return any permutation of T (as a string) that satisfies this property.

Example :
Input: 
S = "cba"
T = "abcd"
Output: "cbad"
Explanation: 
"a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" 
are also valid outputs.

****************************************************************************************/
 '''
#Self solution
def customSortString(S: str, T: str) -> str:
        return "".join(sorted(T,key = lambda x:self.indexOf(x,S)))
    
def indexOf(char,S):
    
    try:
        return S.index(char)
    except:
        return -1

#Pythonic solution
def customSortString(S: str, T: str) -> str:
    counterT = collections.Counter(T)
    
    result = ""
    
    for char in S:
        if char in counterT:
            result += char*counterT[char]

    for char in T:
        if char not in S:
            result += char
    return result