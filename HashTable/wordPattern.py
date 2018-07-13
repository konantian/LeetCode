#Source : https://leetcode.com/problems/word-pattern/
#Author : Yuan Wang
#Date   : 2018-07-13
'''
********************************************************************************** 
*Given a pattern and a string str, find if str follows the same pattern.
*
*Here follow means a full match, such that there is a bijection between a letter 
*in pattern and a non-empty word in str.
*
*Example 1:
*
*Input: pattern = "abba", str = "dog cat cat dog"
*Output: true
*Example 2:
*
*Input:pattern = "abba", str = "dog cat cat fish"
*Output: false
**********************************************************************************/
'''

#Time complexity:O(n) Space complexity:O(1)

def wordPattern(pattern, str):
	"""
	:type pattern: str
	:type str: str
	:rtype: bool
	"""
	str_list=str.split()
	dic={}
	dic_str={}
	for i,word in enumerate(pattern):
		if word in dic:
			dic[word].append(i)
		else:
			dic[word]=[i]
	
	for i,word in enumerate(str_list):
		if word in dic_str:
			dic_str[word].append(i)
		else:
			dic_str[word]=[i]
	
	if len(dic) != len(dic_str):
		return False
	for i in dic:
		if dic[i] not in dic_str.values():
			return False
	return True

pattern="abba"
str="dog cat cat dog"
print(wordPattern(pattern,str))