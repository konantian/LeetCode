
#Source : https://leetcode.com/problems/single-number/
#Author : Yuan Wang
#Date   : 2018-06-26
'''
********************************************************************************** 
*Given a non-empty array of integers, every element appears twice except for one. Find that single one.
*
*Note:
*
*Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
*
*Example 1:
*
*Input: [2,2,1]
*Output: 1
*Example 2:
*
*Input: [4,1,2,1,2]
*Output: 4
**********************************************************************************/
'''
#self solution using dictionary, Time complexity:O(n) Space complexity:O(n)
def singleNumber(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	dic=dict(collections.Counter(nums))
	for i in dic:
		if dic[i] == 1:
	return i

#Other solution using bit manipulation, Time complexity:O(n), Space complexity:O(1)
'''
we use bitwise XOR, XOR is commutative to solve this problem :

first , we have to know the bitwise XOR in java

0 ^ N = N
N ^ N = 0
So..... if N is the single number

N1 ^ N1 ^ N2 ^ N2 ^..............^ Nx ^ Nx ^ N

= (N1^N1) ^ (N2^N2) ^..............^ (Nx^Nx) ^ N

= 0 ^ 0 ^ ..........^ 0 ^ N

= N
'''
def singleNumber(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	first=n0
	for i in range(len(nums)):
		first=first ^ nums[i]
	
	return first

nums=[4,1,2,1,2]
print(singleNumber(nums))



