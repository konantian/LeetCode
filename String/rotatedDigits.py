
#Source : https://leetcode.com/problems/rotated-digits/
#Author : Yuan Wang
#Date   : 2018-06-29
'''
********************************************************************************** 
*X is a good number if after rotating each digit individually by 180 degrees, 
*we get a valid number that is different from X.  Each digit must be rotated - 
*we cannot choose to leave it alone.
*
*A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate 
*to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the 
*rest of the numbers do not rotate to any other number and become invalid.
*
*Now given a positive number N, how many numbers X from 1 to N are good?
*
*Example:
*Input: 10
*Output: 4
*Explanation: 
*There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
*Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
**********************************************************************************/
'''

#Self solution, Time complexity:O(n^2), Space complexity:O(n)
def rotatedDigits(N):
	"""
	:type N: int
	:rtype: int
	"""
	count=0
	original=['0','1','2','5','6','8','9']
	after=['0','1','5','2','9','8','6']
	dic=dict(zip(original,after))
	for i in range(1,N+1):
		number=str(i)
		temp=""
		if "3" in number or "4" in number or "7" in number:
			continue
		for x in number:
			test=dic[x]
			if test:
				temp+=test
	
		if temp != number:
			count+=1
	
	return count


#Other solution, Time complexity:O(n), Space complexity:O(1)
def rotatedDigits(N):
	"""
	:type N: int
	:rtype: int  2 5 6 9 
	"""
	count = 0
	for i in range(1,N+1):
		i = str(i)
		if '3'in i or '4'in i or '7' in i:
			continue
		if '2'in i or '5'in i or '9' in i or '6' in i:
			count +=1
	return count  

N=50
print(rotatedDigits(N))
