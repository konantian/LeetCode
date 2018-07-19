'''
Source : https://leetcode.com/problems/string-compression/
Author : Yuan Wang
Date   : 2018-07-19

/*************************************************************************************** 
*Given an array of characters, compress it in-place.
*
*The length after compression must always be smaller than or equal to the original array.
*
*Every element of the array should be a character (not int) of length 1.
*
*After you are done modifying the input array in-place, return the new length of the array.
*
*Follow up:
*Could you solve it using only O(1) extra space?
*
*
*Example 1:
*Input:
*["a","a","b","b","c","c","c"]
*
*Output:
*Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
*
*Explanation:
*"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
*
****************************************************************************************/
'''

#Self solution, Time complexity:O(n) Space complexity:O(n)
def compress(chars):
	"""
	:type chars: List[str]
	:rtype: int
	"""
	if len(chars) == 1:
		return 1
	index=[(0,chars[0])]
	index+=[(i,char) for i,char in enumerate(chars[1:],start=1) if char != chars[i-1]]
	index.append((len(chars)-1,chars[-1]))
	element=0
	count=1
	for i in range(1,len(index)):
		chars[element]=index[i-1][1]
		length=index[i][0]-index[i-1][0] if index[i][1] != index[i-1][1] else index[i][0]-index[i-1][0]+1
		if 1 < length < 10:
			chars[count]=str(length)
			element+=2
			count+=2
		elif length >= 10:
			chars[count]=str(length)[0]
			chars[count+1]=str(length)[1]
			element+=3
			count+=3
		else:
			element+=1
			count+=1
	return count-1
