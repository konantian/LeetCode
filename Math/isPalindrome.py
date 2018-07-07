
#Source : https://leetcode.com/problems/palindrome-number/
#Author : Yuan Wang
#Date   : 2018-07-07
'''
********************************************************************************** 
*Determine whether an integer is a palindrome. An integer is a palindrome when it 
*reads the same backward as forward.
*
*Example 1:
*
*Input: 121
*Output: true
*Example 2:
*
*Input: -121
*Output: false
*Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
*Therefore it is not a palindrome.
*Example 3:
*
*Input: 10
*Output: false
*Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
**********************************************************************************/
'''

#Self solution, convert the integer to string first
def isPalindrome(x):
	"""
	:type x: int
	:rtype: bool
	"""
	x=str(x)
	return x == x[::-1]

#Other solution, flip the integer from the right to the left and compare if the 
#flipped number is equal to the original number
def isPalindromeB(x):
	"""
	:type x: int
	:rtype: bool
	"""
	if x < 0:
		return False
	elif 0<=x<10:
		return True
	
	temp=x
	rec=0
	while(temp>0):
		rec=rec*10+temp%10
		temp=temp//10
	
	return x == rec

x=1221
print(isPalindromeB(x))