'''
Source : https://leetcode.com/problems/longest-common-prefix/
Author : Yuan Wang
Date   : 2018-06-22

/********************************************************************************** 
*Write a function to find the longest common prefix string amongst an array of strings.
*
*If there is no common prefix, return an empty string "".
*
*Example 1:
*
*Input: ["flower","flow","flight"]
*Output: "fl"
*Example 2:
*
*Input: ["dog","racecar","car"]
*Output: ""
*Explanation: There is no common prefix among the input strings.
**********************************************************************************/
'''

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs or not strs[0]:
        return ""
    start=0
    end=len(strs[0])
    element=strs[0][start]
    result=""
    while self.check_str(element,strs,start) and start<end:
        result+=element
        start+=1
        if start<end:
            element=strs[0][start]
        else:
            break
    
    return result
    
def check_str(element,strs,start):
    for i in range(1,len(strs)):
        if start < len(strs[i]):
            if strs[i][start] != element:
                return False
        else:
            return False
    
    return True

strs=["flower","flow","flight"]
print(longestCommonPrefix(strs))