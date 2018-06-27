#Source : https://leetcode.com/problems/number-of-segments-in-a-string/description/
#Author : Yuan Wang
#Date   : 2018-06-27
'''
********************************************************************************** 
*Count the number of segments in a string, where a segment is defined to be a 
*contiguous sequence of non-space characters.
*
*Please note that the string does not contain any non-printable characters.
*
*Example:
*
*Input: "Hello, my name is John"
*Output: 5
**********************************************************************************/
'''
#Pythonic
def countSegments(s):
	"""
	:type s: str
	:rtype: int
	"""

	return len(s.split())

#Other solution, Time complexity:O(n), Space complexity:O(1)
def countSegments(s):
	"""
	:type s: str
	:rtype: int
	"""
	count=0
	for i in range(len(s)):
		if s[i] != " " and (i==0 or s[i-1]==" "):
			count+=1
	return count


#Self solution,using list comprehension to list all the index of the characters that
#not empty, iterate the list of indexes, if there is gap between any two index means
#there is space between them, then count+1, and return the result of count+1 as the
#final length, Time complexity:O(n), Space complexity:O(n)
def countSegments(s):
	"""
	:type s: str
	:rtype: int
	"""
	count=0
	str_list=[i for i in range(len(s)) if s[i] !=" "]
	if not str_list:
		return 0
	
	for i in range(len(str_list)-1):
		if str_list[i]+1 != str_list[i+1]:
		count+=1
	
	return count+1

#Self solution 2, Time complexity:O(n), Space complexity:O(1)
def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        if len(s)==1 and s[0] != " ":
            n=1
        elif len(s)==1 and s[0] == " ":
            return 0
        else:
            n=len(s)-1
            
        count=0
        counter=False
        for i in range(n):
            if s[i] != " ":
                counter=True
                
            if s[i] ==" " and s[i+1] !=" " and counter==True:
                count+=1
        if counter == False:
            return 0
        
        elif count==True and count == 0:
            return 1
        
        return count+1

s="   Hello, my name   is     John   "
print(countSegments(s))