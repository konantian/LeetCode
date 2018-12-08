
'''
#Source : https://leetcode.com/problems/sqrtx/
#Author : Yuan Wang
#Date   : 2018-12-08

********************************************************************************** 
*Implement int sqrt(int x).
*
*Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
*
*Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
*
*Example 1:
*
*Input: 4
*Output: 2
*Example 2:
*
*Input: 8
*Output: 2
*Explanation: The square root of 8 is 2.82842..., and since 
*the decimal part is truncated, 2 is returned.
**********************************************************************************/
'''

#Newton's method
def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    if x <= 0:
        return x
    x0=x
    hk=0
    while 1:
        hk=(pow(x0,2)-x)/(2*x0)
        x0 -= hk
        if hk < 0.1:
            break
                
    return int(x0)

#Other solution, binary search
def mySqrtB(x):
    l, r = 0, x
    while l <= r:
        mid = l + (r-l)//2
        if mid * mid <= x < (mid+1)*(mid+1):
            return mid
        elif x < mid * mid:
            r = mid
        else:
            l = mid + 1

print(mySqrt(8))