#Source : https://leetcode.com/problems/reverse-integer/
#Author : Yuan Wang
#Date   : 2018-07-05
'''
********************************************************************************** 
*Given a 32-bit signed integer, reverse digits of an integer.
*
*Example 1:
*
*Input: 123
*Output: 321
*Example 2:
*
*Input: -123
*Output: -321
*Example 3:
*
*Input: 120
*Output: 21
*Note:
*Assume we are dealing with an environment which could only store integers within 
*the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem,
*assume that your function returns 0 when the reversed integer overflows.
**********************************************************************************/
'''
#More pythonic solution
def reverse(self, x: int) -> int:
	r = x // max(1,abs(x)) * int(str(abs(x))[::-1])
	return r if r.bit_length() < 32 or r == -2 ** 31 else 0
        
#Pythonic solution
def reverseIntegerA(x):
	"""
	:type x: int
	:rtype: int
	"""
	
	n=str(x)
	if x >= 0:
		result=int(n[::-1])
		return 0 if result > pow(2,31)-1 else result

	else:
		result=int("-"+n[1:][::-1])
		return 0 if result < -pow(2,31) else result


#Self solution
def reverseIntegerB(x):
	"""
	:type x: int
	:rtype: int
	"""
	if x == 0:
		return 0
	n=str(x)
	start=False
	if x> 0:
		result=""
		for i in range(len(n)-1,-1,-1):
			if n[i] != "0":
				result+=n[i]
				start=True
			elif n[i] == "0" and start == True:
				result+=n[i]
	
		result=int(result)   
		return 0 if result > pow(2,31)-1 else result
	else:
		result="-"
		for i in range(len(n)-1,0,-1):
			if n[i] != "0":
				result+=n[i]
				start=True
			elif n[i] == "0" and start == True:
				result+=n[i]
		result=int(result)  
		return 0 if result < -pow(2,31) else result


x=-12345
print(reverseIntegerB(x))
