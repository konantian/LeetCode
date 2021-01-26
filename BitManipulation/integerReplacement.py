'''
Source : https://leetcode.com/problems/integer-replacement/
Author : Yuan Wang
Date   : 2021-01-26

/*************************************************************************************** 
*Given a positive integer n, you can apply one of the following operations:
*
*If n is even, replace n with n / 2.
*If n is odd, replace n with either n + 1 or n - 1.
*Return the minimum number of operations needed for n to become 1.
*Example1 :
*Input: n = 8
*Output: 3
*Explanation: 8 -> 4 -> 2 -> 1
****************************************************************************************/
 '''
 
#Recursive solution, time complexity : O(n)
def integerReplacement(self, n: int, counter = 0) -> int:
    if n == 1: return counter
    if not n%2: return self.integerReplacement(n/2, counter+1)
    else: return min(self.integerReplacement(n+1, counter+1), self.integerReplacement(n-1, counter+1))
    
    
#Iterative solution, time complexity: O(logn)
def integerReplacement(self, n: int, counter = 0) -> int:
    count = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            if n & 2 and n != 3:
                n += 1
            else:
                n -= 1
        
        count += 1
    
    return count