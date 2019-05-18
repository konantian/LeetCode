'''
Source : https://leetcode.com/problems/find-all-duplicates-in-an-array/
Author : Yuan Wang
Date   : 2019-05-17

/*************************************************************************************** 
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
  
****************************************************************************************/
 '''
#Self solution
def findAndReplacePattern(words: List[str], pattern: str) -> List[str]:
    result = []
    for word in words:
        if self.findHelper(word,pattern):
            result.append(word)
    return result

def findHelper(word,pattern):
    dic = {}
    for i in range(len(pattern)):
        if pattern.count(pattern[i]) != word.count(word[i]):
            return False
        else:
            if pattern[i] not in dic:
                dic[pattern[i]] = word[i]
            else:
                if dic[pattern[i]] != word[i]:
                    return False
    return True

#Pythonic solution
def findAndReplacePattern(self, words, pattern):
    def match(word):
        m1, m2 = {}, {}
        for w, p in zip(word, pattern):
            if w not in m1: m1[w] = p
            if p not in m2: m2[p] = w
            if (m1[w], m2[p]) != (p, w):
                return False
        return True

    return filter(match, words)