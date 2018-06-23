
#Source : https://leetcode.com/problems/add-binary/
#Author : Yuan Wang
#Date   : 2018-06-23
'''
********************************************************************************** 
*Given two binary strings, return their sum (also a binary string).
*
*The input strings are both non-empty and contains only characters 1 or 0.
*
*Example 1:
*
*Input: a = "11", b = "1"
*Output: "100"
*Example 2:
*
*Input: a = "1010", b = "1011"
*Output: "10101"
**********************************************************************************/
'''

#Pythonic
def addBinary(a, b):
	"""
	:type a: str
	:type b: str
	:rtype: str
	"""
	return bin(int(a,2)+int(b,2))[2:]

#self solution
def addBinaryB(a, b):
	"""
	:type a: str
	:type b: str
	:rtype: str
	"""
	a_decimal=0
	b_decimal=0
	for i,num in enumerate(a):
		if num == '1':
			a_decimal+=pow(2,len(a)-i-1)
	for x,num in enumerate(b):
		if num == '1':
			b_decimal+=pow(2,len(b)-x-1)
	
	result=a_decimal+b_decimal
	if result == 0:
		return "0"
	last=""
	while(result>=1):
		last+=str(result%2)
		result=result//2
	
	return last[::-1]

print(addBinary("1010","1011"))