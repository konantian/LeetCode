'''
Source : https://leetcode.com/problems/positions-of-large-groups/
Author : Yuan Wang
Date   : 2018-06-17

/********************************************************************************** 
*In a string S of lowercase letters, these letters form consecutive groups of the same character.
*
*For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".
*
*Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.
*
*The final answer should be in lexicographic order.
*
*
*
*Example 1:
*
*Input: "abbxxxxzzy"
*Output: [[3,6]]
*Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.
*Example 2:
*
*Input: "abc"
*Output: []
*Explanation: We have "a","b" and "c" but no large group.
*Example 3:
*
*Input: "abcdddeeeeaabbbcd"
*Output: [[3,5],[6,9],[12,14]]
**********************************************************************************/
'''

def largeGroupPositions(S):
	"""
	:type S: str
	:rtype: List[List[int]]
	"""
	d={}
	result=[]
	for i,string in enumerate(S):
		if string not in d:
			d[string]=[[i]]
		else:
			if d[string][-1][-1]+1==i:
				d[string][-1].append(i)
			else:
				d[string].append([i])
	
	for key in d:
		for i in d[key]:
			if len(i) >=3:
				result.append([i[0],i[-1]])
	
	return sorted(result,key=lambda result : result[0])

def largeGroupPositionsB(S):
	i, j, N = 0, 0, len(S)
	res = []
	while j < N:
		while j < N and S[j] == S[i]: j += 1
		if j - i >= 3: res.append((i, j - 1))
		i = j
	return res
	
S="abcdddeeeeaabbbcd"
print(largeGroupPositions(S))