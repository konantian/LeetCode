'''
Source : https://leetcode.com/problems/to-lower-case/
Author : Yuan Wang
Date   : 2018-07-17

/*************************************************************************************** 
*Implement function ToLowerCase() that has a string parameter str, and returns the same 
*string in lowercase.
*
* 
*
*Example 1:
*
*Input: "Hello"
*Output: "hello"
*Example 2:
*
*Input: "here"
*Output: "here"
*Example 3:
*
*Input: "LOVELY"
*Output: "lovely" 
****************************************************************************************/
 '''

#Using python built-in function:
def toLowerCase(str):
	"""
	:type str: str
	:rtype: str
	"""
	return str.lower()

#Using ascii table 
def toLowerCaseB(str):
	"""
	:type str: str
	:rtype: str
	"""
	result=""
	for i in str:
		index=ord(i)
		if 65<=index<=90:
			result+=chr(index+32)
		else:
			result+=i
	return result


str="Hello"
print(toLowerCaseB(str))