
#Source : https://leetcode.com/problems/first-unique-character-in-a-string/
#Author : Yuan Wang
#Date   : 2018-06-24
'''
********************************************************************************** 
*Given a string, find the first non-repeating character in it and return it's index.
*If it doesn't exist, return -1.
*
*Examples:
* 
*s = "leetcode"
*return 0.
*
*s = "loveleetcode",
*return 2.
**********************************************************************************/
'''
#self solution, using dictionary and set, Time complexity:O(n) Space complexity:O(n)
#Drawbacks: using too much extra space to store temp elements
def firstUniqChar(s):
	"""
	:type s: str
	:rtype: int
	"""
	if not s:
		return -1
	dic={}
	deleted=set([])
	for i,char in enumerate(s):
		if char not in dic and char not in deleted:
			dic[char]=i
		else:
			if char not in deleted:
				deleted.add(char)
				del dic[char]

	if not dic:
		return -1
	
	return min(dic.values())

#Other solution
def firstUniqCharB(s):
	"""
	:type s: str
	:rtype: int
	"""
	letter = "abcdefghijklmnopqrstuvwxyz"
	letters=set(letter)
	unique = [s.index(l) for l in letters if s.count(l) == 1]
	return -1 if len(unique) == 0 else min(unique)

s="loveleetcode"
print(firstUniqCharB(s))

