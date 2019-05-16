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


def findMedianSortedArrays(A, B):
    m, n = len(A), len(B)
    if m > n:
        A, B, m, n = B, A, n, m
    if n == 0:
        raise ValueError

    imin, imax, half_len = 0, m, (m + n + 1) / 2
    while imin <= imax:
        i = (imin + imax) / 2
        j = half_len - i
        if i < m and B[j-1] > A[i]:
            # i is too small, must increase it
            imin = i + 1
        elif i > 0 and A[i-1] > B[j]:
            # i is too big, must decrease it
            imax = i - 1
        else:
            # i is perfect

            if i == 0: max_of_left = B[j-1]
            elif j == 0: max_of_left = A[i-1]
            else: max_of_left = max(A[i-1], B[j-1])

            if (m + n) % 2 == 1:
                return max_of_left

            if i == m: min_of_right = B[j]
            elif j == n: min_of_right = A[i]
            else: min_of_right = min(A[i], B[j])

            return (max_of_left + min_of_right) / 2.0





