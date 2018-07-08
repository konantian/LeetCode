
#Source : https://leetcode.com/problems/excel-sheet-column-number/
#Author : Yuan Wang
#Date   : 2018-07-08
'''
********************************************************************************** 
*Given a column title as appear in an Excel sheet, return its corresponding column number.
*
*For example:
*
*	A -> 1
*	B -> 2
*	C -> 3
*	...
*	Z -> 26
*	AA -> 27
*	AB -> 28 
*	...
*Example 1:
*
*Input: "A"
*Output: 1
*Example 2:
*
*Input: "AB"
*Output: 28
*Example 3:
*
*Input: "ZY"
*Output: 701
**********************************************************************************/
'''

def titleToNumber(s):
	"""
	:type s: str
	:rtype: int
	"""
	number=0
	alphabet=list(string.ascii_uppercase)
	value=range(1,27)
	dic=dict(zip(alphabet,value))
	for i in range(len(s)):
		number+=dic[s[i]]*pow(26,len(s)-i-1)
	
	return number

s="ZY"
print(titleToNumber(s))