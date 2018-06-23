
#Source : https://leetcode.com/problems/ransom-note/
#Author : Yuan Wang
#Date   : 2018-06-23
'''
********************************************************************************** 
*Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
*
*Each letter in the magazine string can only be used once in your ransom note.
*
*Note:
*You may assume that both strings contain only lowercase letters.
*
*canConstruct("a", "b") -> false
*canConstruct("aa", "ab") -> false
*canConstruct("aa", "aab") -> true
**********************************************************************************/
'''
#Self solution A,Time complexity:O(n), Space Complexity:O(n)
def canConstructA(ransomNote, magazine):
	"""
	:type ransomNote: str
	:type magazine: str
	:rtype: bool
	"""
	magazine=dict(collections.Counter(magazine))
	ransomNote=dict(collections.Counter(ransomNote))
	for i in ransomNote:
		try:
			if ransomNote[i] > magazine[i]:
				return False
		except:
			return False
	return True

#Self solution B,Time complexity:O(n), Space Complexity:O(n)
def canConstructB(ransomNote, magazine):
	"""
	:type ransomNote: str
	:type magazine: str
	:rtype: bool
	"""
	magazine=dict(collections.Counter(magazine))
	for i in ransomNote:
		if i in magazine:
			if magazine[i] > 0:
				magazine[i]-=1
			else:
				return False
		else:
	 		return False
	return True

#Other suliton using set
def canConstruct(ransomNote, magazine):
	"""
	:type ransomNote: str
	:type magazine: str
	:rtype: bool
	"""
	for i in set(ransomNote):
		if ransomNote.count(i) > magazine.count(i):
			return False
	return True

ransomNote="aa"
magazine="aab"
print(canConstruct(ransomNote,magazine))


