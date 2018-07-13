#Source : https://leetcode.com/problems/longest-palindrome/
#Author : Yuan Wang
#Date   : 2018-07-13
'''
********************************************************************************** 
*Given a string which consists of lowercase or uppercase letters, find the length 
*of the longest palindromes that can be built with those letters.
*
*This is case sensitive, for example "Aa" is not considered a palindrome here.
*
*Note:
*Assume the length of given string will not exceed 1,010.
*
*Example:
*
*Input:
*"abccccdd"
*
*Output:
*7
*
*Explanation:
*One longest palindrome that can be built is "dccaccd", whose length is 7.
**********************************************************************************/
'''

#Time complexity:O(n) Space complexity:O(1)
def longestPalindrome(s):
	"""
	:type s: str
	:rtype: int
	"""
	dic=dict(collections.Counter(s))
	count=0
	even_test=False
	odd_test=False
	for i in dic:
		if dic[i] % 2 == 0:
			count+=dic[i]
			even_test=True
		else:
			count+=dic[i]//2*2
			odd_test=True
	
	return count+1 if odd_test == True else count

s="abccccdd"
print(longestPalindrome(s))


