'''
Source : https://leetcode.com/problems/fibonacci-number/
Author : Yuan Wang
Date   : 2019-05-16

/********************************************************************************** 
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci
 sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).
**********************************************************************************/
'''
#DP solution using for loop
def fib(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        numbers = [0,1]
        for i in range(N-len(numbers)+1):
            numbers.append(numbers[-1]+numbers[-2])
        return numbers[-1]

#DP solution using recursive
def fib2(N: int) -> int:
        if N < 2: return N
        else:
            return fib_helper(N,[0,1])
        
def fib_helper(N,result):
    if N == 1:
        return result[-1]
    result.append(result[-1]+result[-2])
    return fib_helper(N-1,result)

#Other solution Space complexity:O(1)
def fib3(N):
    a,b = 0,1
    for _ in range(N):
        a, b = b, a+b
    return a 


print(fib(10))




