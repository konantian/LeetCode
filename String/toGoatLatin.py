
#Source : https://leetcode.com/problems/goat-latin/
#Author : Yuan Wang
#Date   : 2018-07-01
'''
********************************************************************************** 
*A sentence S is given, composed of words separated by spaces. Each word consists 
*of lowercase and uppercase letters only.
*
*We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)
*
*The rules of Goat Latin are as follows:
*
*If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
*For example, the word 'apple' becomes 'applema'.
* 
*If a word begins with a consonant (i.e. not a vowel), remove the first letter and 
*append it to the end, then add "ma".
*For example, the word "goat" becomes "oatgma".
* 
*Add one letter 'a' to the end of each word per its word index in the sentence, 
*starting with 1.
*For example, the first word gets "a" added to the end, the second word gets "aa" 
*added to the end and so on.
*Return the final sentence representing the conversion from S to Goat Latin. 
**********************************************************************************/
'''

#Self solution
def toGoatLatin(S):
	"""
	:type S: str
	:rtype: str
	"""
	count=1
	sentences=S.split()
	for i in range(len(sentences)):
		if sentences[i][0].lower() in "aeiou":
			sentences[i]+="ma"+count*"a"
		else:
			sentences[i]=sentences[i][1:]+sentences[i][0]+'ma'+count*"a"
			count+=1
	
	return " ".join(sentences)

S="The quick brown fox jumped over the lazy dog"
print(toGoatLatin(S))