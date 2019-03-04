'''
Source : https://leetcode.com/problems/sum-of-even-numbers-after-queries/
Author : Yuan Wang
Date   : 2019-03-03

/********************************************************************************** 
We have an array A of integers, and an array queries of queries.

For the i-th query val = queries[i][0], index = queries[i][1], we add val to A[index].
Then, the answer to the i-th query is the sum of the even values of A.

(Here, the given index = queries[i][1] is a 0-based index, and each query permanently
modifies the array A.)

Return the answer to all queries.  Your answer array should have answer[i] as the answer
to the i-th query.

Example 1:

Input: A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
Output: [8,6,2,4]
Explanation: 
At the beginning, the array is [1,2,3,4].
After adding 1 to A[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
After adding -3 to A[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
After adding -4 to A[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
After adding 2 to A[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.
**********************************************************************************/
'''

#Time Complexity: O(N+Q), where N is the length of A and Q is the number of queries.

#Space Complexity: O(Q), though we only allocate O(1) additional space. 
#Self solution
def sumEvenAfterQueries(A, queries):
    result=[]
    """
    :type A: List[int]
    :type queries: List[List[int]]
    :rtype: List[int]
    """
    even_sum = sum([i for i in A if i % 2 == 0])
    for i in queries:
        val,index=i
        previous = A[index]
        A[index] += val
        if previous % 2 != 0 and A[index] % 2 == 0:
            even_sum += A[index]
        elif previous % 2 == 0 and A[index] % 2 !=0:
            even_sum -= previous
        elif previous % 2 == 0 and A[index] % 2 == 0:
            even_sum += val
        result.append(even_sum)
        
    return result


#Other solution with less time
def sumEvenAfterQueries(A, queries):
    result=[]
    """
    :type A: List[int]
    :type queries: List[List[int]]
    :rtype: List[int]
    """
    even_sum = sum([i for i in A if i % 2 == 0])
    for val,index in queries:
        previous = A[index]
        
        if previous % 2 == 0:
            even_sum -= previous
        A[index] += val
        if A[index] % 2 == 0:
            even_sum += A[index]
        result.append(even_sum)
        
    return result


