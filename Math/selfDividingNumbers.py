#Source : https://leetcode.com/problems/self-dividing-numbers/
#Author : Yuan Wang
#Date   : 2019-05-21
'''
********************************************************************************** 
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing
 number, including the bounds if possible.

Example 1:
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
**********************************************************************************/
'''

def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        result = [i for i in range(left,right+1) if self.canDividByItself(i)]
        return result
    
def canDividByItself(self,n):
    t = n
    while t > 0:
        digit = t % 10
        if digit == 0 or n % digit != 0:
            return False
        t = t // 10
        
    return True