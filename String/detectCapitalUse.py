
#Source : https://leetcode.com/problems/detect-capital/
#Author : Yuan Wang
#Date   : 2018-06-27
'''
********************************************************************************** 
*Given a word, you need to judge whether the usage of capitals in it is right or not.
*
*We define the usage of capitals in a word to be right when one of the following cases holds:
*
*1.All letters in this word are capitals, like "USA".
*2.All letters in this word are not capitals, like "leetcode".
*3.Only the first letter in this word is capital if it has more than one letter, like "Google".
*Otherwise, we define that this word doesn't use capitals in a right way.
*Example 1:
*Input: "USA"
*Output: True
*Example 2:
*Input: "FlaG"
*Output: False
**********************************************************************************/
'''

#Pythonic
def detectCapitalUse(word):
	"""
	:type word: str
	:rtype: bool
	"""
	return word.isupper() or word.islower() or word.istitle()
#Self solution, Time complexity:O(n), Space complexity:O(1)
def detectCapitalUse(word):
	"""
	:type word: str
	:rtype: bool
	"""
	if not word:
		return False
	elif len(word) == 1:
		return True
	
	else:
		if word.lower()==word or word.upper()==word:
			return True
		elif 65<=ord(word[0])<=90 and word[1:].lower()==word[1:]:
			return True
		else:
			return False

words=["g","USA","China","FlaG"]
print(*list(map(detectCapitalUse,words)),sep='\n')