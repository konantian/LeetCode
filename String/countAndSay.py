
#Source : https://leetcode.com/problems/count-and-say/
#Author : Yuan Wang
#Date   : 2018-07-04
'''
********************************************************************************** 
*The count-and-say sequence is the sequence of integers with the first five terms as following:
*
*1.	 1
*2.	 11
*3.	 21
*4.	 1211
*5.	 111221
*1 is read off as "one 1" or 11.
*11 is read off as "two 1s" or 21.
*21 is read off as "one 2, then one 1" or 1211.
*Given an integer n, generate the nth term of the count-and-say sequence.
*
*Note: Each term of the sequence of integers will be represented as a string.
*
*Example 1:
*
*Input: 1
*Output: "1"
*Example 2:
*
*Input: 4
*Output: "1211"
**********************************************************************************/
'''

#Self solution one,slow
def countAndSayA(n):
	"""
	:type n: int
	:rtype: str
	"""
	sample=["1","11","21","1211","111221"]
	if n <= 5:
		return sample[n-1]
	
	for x in range(5,n):
		result=""
		string=sample[x-1]
		initial=string[0]
		count=0
		for i in range(len(string)):
			if string[i] == initial:
				count+=1
				if i == len(string)-1:
					result+=str(count)+str(initial)
	
			else:
				result+=str(count)+str(initial)
				initial=string[i]
				count=1
	  
				if i == len(string)-1:
					result+=str(count)+str(initial)
	
		sample.append(result)

	return sample[n-1]

#Self solution two, using recursion
def countAndSayB(n):
	"""
	:type n: int
	:rtype: str
	"""
	if n == 1:
		return "1"
	elif n == 2:
		return "11"
	else:
		string=countAndSay(n-1)
		initial=string[0]
		count=0
		result=""
		for i,char in enumerate(string):
			if char == initial:
				count+=1
				if i == len(string)-1:
					result+=str(count)+str(initial)
	
			else:
				result+=str(count)+str(initial)
				initial=char
				count=1
	  
				if i == len(string)-1:
					result+=str(count)+str(initial)
	
	return result


print(countAndSayB(5))