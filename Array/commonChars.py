'''
Source : https://leetcode.com/problems/find-common-characters/
Author : Yuan Wang
Date   : 2019-05-16

/********************************************************************************** 
Given an array A of strings made only from lowercase letters, return a list of all 
characters that show up in all strings within the list (including duplicates).  
For example, if a character occurs 3 times in all strings but not 4 times, you need
 to include that character three times in the final answer.

You may return the answer in any order.
Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]
 
**********************************************************************************/
'''
import collections
#self solution
def commonChars(A: List[str]) -> List[str]:
        
        import functools
        
        tempString = functools.reduce(intercetTwoString,A)
        return list(tempString)
    
def intercetTwoString(A,B):
    result=""
    A = collections.Counter(A)
    B = collections.Counter(B)
    for char in A:
        for i in range(min(A[char],B[char])):
            result += char
    return result

#Other pythonic solution
def commonChars(A: List[str]) -> List[str]:
        
    res = collections.Counter(A[0])
    
    for a in A[1:]:
        res &= collections.Counter(a)
    return list(res.elements())