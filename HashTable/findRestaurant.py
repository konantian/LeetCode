#Source : https://leetcode.com/problems/minimum-index-sum-of-two-lists/
#Author : Yuan Wang
#Date   : 2018-07-10
'''
********************************************************************************** 
*Suppose Andy and Doris want to choose a restaurant for dinner, and they both have 
*a list of favorite restaurants represented by strings.
*
*You need to help them find out their common interest with the least list index sum.
*If there is a choice tie between answers, output all of them with no order requirement.
*You could assume there always exists an answer.
*
*Example 1:
*Input:
*["Shogun", "Tapioca Express", "Burger King", "KFC"]
*["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
*Output: ["Shogun"]
*Explanation: The only restaurant they both like is "Shogun".
*Example 2:
*Input:
*["Shogun", "Tapioca Express", "Burger King", "KFC"]
*["KFC", "Shogun", "Burger King"]
*Output: ["Shogun"]
*Explanation: The restaurant they both like and have the least index sum is "Shogun"
*with index sum 1 (0+1).
**********************************************************************************/
'''

#Time complexity:O(n), Space complexity:O(n)
def findRestaurant(list1, list2):
	"""
	:type list1: List[str]
	:type list2: List[str]
	:rtype: List[str]
	"""
	index1={x:i for i,x in enumerate(list1)}
	index2={x:i for i,x in enumerate(list2)}
	result=[]
	total=float('inf')
	for i in index1:
		if i in index2:
			temp=index1[i]+index2[i]
			if temp < total:
				total=temp
				result=[i]
			elif temp == total:
				total=temp
				result.append(i)
	return result

list1=["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2=["KFC", "Shogun", "Burger King"]
print(findRestaurant(list1,list2))