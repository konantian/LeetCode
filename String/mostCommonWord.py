
#Source : https://leetcode.com/problems/most-common-word/
#Author : Yuan Wang
#Date   : 2018-07-02
'''
********************************************************************************** 
*Given a paragraph and a list of banned words, return the most frequent word that is 
*not in the list of banned words.  It is guaranteed there is at least one word that 
*isn't banned, and that the answer is unique.
*
*Words in the list of banned words are given in lowercase, and free of punctuation. 
*Words in the paragraph are not case sensitive.  The answer is in lowercase.
*
*Example:
*Input: 
*paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
*banned = ["hit"]
*Output: "ball"
*Explanation: 
*"hit" occurs 3 times, but it is a banned word.
*"ball" occurs twice (and no other word does), so it is the most frequent non-banned 
*word in the paragraph. 
*Note that words in the paragraph are not case sensitive,
*that punctuation is ignored (even if adjacent to words, such as "ball,"), 
*and that "hit" isn't the answer even though it occurs more because it is banned.
**********************************************************************************/
'''

def mostCommonWord(paragraph, banned):
	"""
	:type paragraph: str
	:type banned: List[str]
	:rtype: str
	"""
	banned=set(banned)
	para_list=paragraph.split()
	para_list=[''.join(filter(str.isalpha, i)).lower() for i in para_list] #delete any characters that not letter

	para_list=[i for i in para_list if i.lower() not in banned]

	dic=collections.Counter(para_list)
	
	return dic.most_common(1)[0][0] #return the element that has highest count


paragraph="Bob hit a ball, the hit BALL flew far after it was hit."
banned=["hit"]

print(mostCommonWord(paragraph,banned))