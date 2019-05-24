#Source : https://leetcode.com/problems/subsets/
#Author : Yuan Wang
#Date   : 2019-05-23
'''
********************************************************************************** 
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
**********************************************************************************/
'''

#pythonic solution
def subsetsA(self, nums: List[int]) -> List[List[int]]:

	import itertools

    result = []
    for n in range(len(nums)+1):
        items = [i for i in itertools.combinations(nums,n)]
        result += items
    return result


# Iteratively
def subsetsB(self, nums):
    res = [[]]
    for num in sorted(nums):
        res += [item+[num] for item in res]
        print(res)
    return res

subsetsB([1,2,3])

