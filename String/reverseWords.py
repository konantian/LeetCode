
#Source : https://leetcode.com/problems/reverse-words-in-a-string-iii/
#Author : Yuan Wang
#Date   : 2018-07-03
'''
********************************************************************************** 
*Given a string, you need to reverse the order of characters in each word within a 
*sentence while still preserving whitespace and initial word order.
*
*Example 1:
*Input: "Let's take LeetCode contest"
*Output: "s'teL ekat edoCteeL tsetnoc"
**********************************************************************************/
'''
#Pythonic solution	
def reverseWords(s):
	"""
	:type s: str
	:rtype: str
	"""
	lst=s.split()
	return " ".join(i[::-1] for i in lst)

#Self solution
def reverseWords(s):
	"""
	:type s: str
	:rtype: str
	"""
	result=""
	start=0
	index=[i for i in range(len(s)) if s[i] == " "]
	if not index:
		r=list(s)
		i,j=0,len(r)-1
		while i < j:
			r[i],r[j]=r[j],r[i]
			i+=1
			j-=1
		return "".join(r)
	for i in index:
		result+=s[start:i][::-1]+" "
		start=i+1
	result+=s[index[-1]+1:][::-1]
	
	return result


#Other solution
def reverseWords(s):
	"""
	:type s: str
	:rtype: str
	"""
	words = s.split(" ")
	output = ""
	
	for i, word in enumerate(words):
		output += word[::-1]
		if i != len(words) - 1:
			output += " "
	
	return output