# Source : https://oj.leetcode.com/problems/remove-element/
# Author : Yuan Wang
# Date   : 2018-05-27
'''
********************************************************************************** 
* 
* Given an array and a value, remove all instances of that value in place and return the new length.
* 
* The order of elements can be changed. It doesn't matter what you leave beyond the new length.
* 
*  Complexity analysis

Time complexity : O(n). The code only traverse the array once and it takes O(n)
element replacing takes O(1) to execute, in total is O(n)

Space complexity : O(1).
**********************************************************************************/
'''
def removeElementA(nums, val):
	"""
	:type nums: List[int]
	:type val: int
	:rtype: int
	"""
	for i in range(nums.count(val)):
		nums.remove(val)
def removeElementB(nums,val):
	begin=0
	for i in range(len(nums)):
		if nums[i] != val:
			nums[begin]=nums[i]
			begin+=1
	return begin
nums=[0,1,2,2,3,0,4,2]
val=2
begin=removeElementB(nums,val)
print(nums[:begin])