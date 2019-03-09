'''
Source : https://leetcode.com/problems/add-to-array-form-of-integer/
Author : Yuan Wang
Date   : 2019-03-08

/********************************************************************************** 
For a non-negative integer X, the array-form of X is an array of its digits in left
 to right order.  For example, if X = 1231, then the array form is [1,2,3,1].

Given the array-form A of a non-negative integer X, return the array-form of the 
integer X+K.
Example 1:

Input: A = [1,2,0,0], K = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
Example 2:

Input: A = [2,7,4], K = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455
**********************************************************************************/
'''

'''
We can do a variant of the above idea that is easier to implement - we put the entire addend in the first column from the right.

Continuing the example of 123 + 912, we start with [1, 2, 3+912]. Then we perform the addition 3+912, leaving 915. The 5 stays as the digit, while we 'carry' 910 into the next column which becomes 91.

We repeat this process with [1, 2+91, 5]. We have 93, where 3 stays and 90 is carried over as 9. Again, we have [1+9, 3, 5] which transforms into [1, 0, 3, 5].
'''
def addToArrayForm(A, K):
    A[-1] += K
    for i in range(len(A) - 1, -1, -1):
        carry, A[i] = divmod(A[i], 10)
        if i: A[i-1] += carry
    if carry:
        A = map(int, str(carry)) + A
    return A