
#Source : https://leetcode.com/problems/intersection-of-two-arrays-ii/
#Author : Yuan Wang
#Date   : 2018-07-08
'''
********************************************************************************** 
*Given two arrays, write a function to compute their intersection.
*
*Example:
*Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
*
*Note:
*Each element in the result should appear as many times as it shows in both arrays.
*The result can be in any order.
**********************************************************************************/
'''

#Time complexity:O(n), Space complexity:O(n)
def intersect(nums1, nums2):
	"""
	:type nums1: List[int]
	:type nums2: List[int]
	:rtype: List[int]
	"""

	nums1_dic=dict(collections.Counter(nums1))
	nums2_dic=dict(collections.Counter(nums2))
	
	result=[]
	for i in nums2_dic:
		if i in nums1_dic:
			result+=min(nums2_dic[i],nums1_dic[i])*[i]
	
	return result


nums1=[1,2,2,1]
nums2=[2,2]
print(intersect(nums1,nums2))