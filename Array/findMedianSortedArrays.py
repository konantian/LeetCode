'''
Source : https://leetcode.com/problems/median-of-two-sorted-arrays/
Author : Yuan Wang
Date   : 2019-05-14

/********************************************************************************** 
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
**********************************************************************************/
'''

def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    result=[]
    i,j=0,0
    while i<len(nums1) and j<len(nums2):
        if nums1[i]<=nums2[j]:
            result.append(nums1[i])
            i+=1
        else:
            result.append(nums2[j])
            j+=1
    result += nums1[i:]
    result += nums2[j:]
    
    if len(result) % 2 != 0:
        return result[math.floor(len(result)/2)]
    else:
        return (result[int(len(result)/2)]+result[int(len(result)/2-1)])/2





