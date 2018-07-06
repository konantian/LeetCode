
#Source : https://leetcode.com/problems/happy-number/
#Author : Yuan Wang
#Date   : 2018-07-06
'''
********************************************************************************** 
*Write an algorithm to determine if a number is "happy".
*
*A happy number is a number defined by the following process: Starting with any 
*positive integer, replace the number by the sum of the squares of its digits, 
*and repeat the process until the number equals 1 (where it will stay), or it 
*loops endlessly in a cycle which does not include 1. Those numbers for which this 
*process ends in 1 are happy numbers.
*
*Example: 
*
*Input: 19
*Output: true
*Explanation: 
*12 + 92 = 82
*82 + 22 = 68
*62 + 82 = 100
*12 + 02 + 02 = 1
**********************************************************************************/
'''

#Self solution, Time complexity:O(n), Space complexity:O(n)
def isHappy(n):
	"""
	:type n: int
	:rtype: bool
	"""
	total=n
	result=[]
	result=set(result)
	while(1):
		total=sum(pow(int(i),2) for i in str(total))
		if total == 100 or total == 1:
			return True
		elif total in result and 1 not in result:
			return False
	
		else:
			result.add(total)


n=19
print(isHappy(n))