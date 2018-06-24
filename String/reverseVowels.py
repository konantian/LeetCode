
#Source : https://leetcode.com/problems/reverse-vowels-of-a-string/
#Author : Yuan Wang
#Date   : 2018-06-24
'''
********************************************************************************** 
*Write a function that takes a string as input and reverse only the vowels of a string.
*
*Example 1:
*Given s = "hello", return "holle".
*
*Example 2:
*Given s = "leetcode", return "leotcede".
*
*Note:
*The vowels does not include the letter "y".
**********************************************************************************/
'''

#Self solution one,generate a list of all the vowels and reverse them in the list
#order of them and rebuild a string with reversed order of vowels
#Time complexity:O(n), Space complexity:O(n)
def reverseVowelsA(s):
	"""
	:type s: str
	:rtype: str
	"""
	vowels=[string for string in s if string.lower() in"aeiou"]
	lst=set(vowels)
	result=""
	index=len(vowels)-1
	for i in s:
		if i not in lst:
			result+=i
		else:
			result+=vowels[index]
			index-=1
	return result

#self solution two, generate a list of indexes of all vowels
#using two pointer swap each pair of vowels until the middle of the original string
#Time complexity:O(n), Space complexity:O(n)
def reverseVowelsB(s):
	"""
	:type s: str
	:rtype: str
	"""
	vowel=[i for i,char in enumerate(s) if char.lower() in "aeiou"]
	string=list(s)
	for i in range(len(vowel)//2):	  
		string[vowel[i]],string[vowel[len(vowel)-i-1]]=string[vowel[len(vowel)-1-i]],string[vowel[i]]  
	
	return "".join(string)

#Other solution using two pointer
#Time complexity:O(n), Space complexity:O(n)
def reverseVowels(s):
	"""
	:type s: str
	:rtype: str
	"""
	vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
	L = list(s)
	i = 0
	j = len(L) - 1
	while i < j:
		while i < j and L[i] not in vowels:
			i += 1
		while j > i and L[j] not in vowels:
			j -= 1
		L[i], L[j] = L[j], L[i] 
		i += 1
		j -= 1
	return ''.join(L)

print(reverseVowels("hello"))
