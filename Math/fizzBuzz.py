
#Source : https://leetcode.com/problems/fizz-buzz/description/
#Author : Yuan Wang
#Date   : 2018-06-25
'''
********************************************************************************** 
*Write a program that outputs the string representation of numbers from 1 to n.
*
*But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
*
*Example:
*
*n = 15,
*
*Return:
*[
*	"1",
*	"2",
*	"Fizz",
*	"4",
*	"Buzz",
*	"Fizz",
*	"7",
*	"8",
*	"Fizz",
*	"Buzz",
*	"11",
*	"Fizz",
*	"13",
*	"14",
*	"FizzBuzz"
*]
**********************************************************************************/
'''

def fizzBuzz(n):
	"""
	:type n: int
	:rtype: List[str]
	"""
	result=[0]*n
	for i in range(1,n+1):
		if i % 3 == 0:
			if i % 5 == 0:
				result[i-1]="FizzBuzz"
			else:
				result[i-1]="Fizz"
		elif i % 5 == 0:
			result[i-1]="Buzz"
		else:
			result[i-1]=str(i)
	return result

n=15
print(fizzBuzz(n))