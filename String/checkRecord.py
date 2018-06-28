
#Source : https://leetcode.com/problems/student-attendance-record-i/description/
#Author : Yuan Wang
#Date   : 2018-06-28
'''
********************************************************************************** 
*You are given a string representing an attendance record for a student. The record only contains the following three characters:
*'A' : Absent.
*'L' : Late.
*'P' : Present.
*A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).
*
*You need to return whether the student could be rewarded according to his attendance record.
*
*Example 1:
*Input: "PPALLP"
*Output: True
*Example 2:
*Input: "PPALLL"
*Output: False
**********************************************************************************/
'''
#Pythonic
def checkRecordA(s):
	"""
	:type s: str
	:rtype: bool
	"""
	return(s.count("A") < 2 and "LLL" not in s)

#Self solution, Time complexity:O(n) Space complexity:O(1)
def checkRecordB(s):
	"""
	:type s: str
	:rtype: bool
	"""
	A_count=0;L_count=0;inter_count=0
	for i in range(len(s)):
		if s[i] == "L":
			inter_count+=1
		else:
			if s[i] == "A":
				A_count+=1
			inter_count=0
			if A_count > 1 or inter_count >2:
				return False
			L_count = inter_count if inter_count>L_count else L_count
	
	return True

#Other solution using regular expression
def checkRecordC(s):
	"""
	:type s: str
	:rtype: bool
	"""
	import re
	return re.match(".*LLL.*|.*A.*A.*",s) is None


s="PPALLPLL"
print(checkRecordC(s))