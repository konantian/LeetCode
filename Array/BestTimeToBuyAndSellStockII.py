'''
Source : https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
Author : Yuan Wang
Date   : 2018-06-03

/********************************************************************************** 
* 
* Say you have an array for which the ith element is the price of a given stock on day i.
* 
* Design an algorithm to find the maximum profit. You may complete as many transactions 
* as you like (ie, buy one and sell one share of the stock multiple times). However, 
* you may not engage in multiple transactions at the same time (ie, you must sell the 
* stock before you buy again).
*	  
* Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
	 Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
	 Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
	 engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
**********************************************************************************/
'''

#Time complexity: O(n), Space complexity: O(1)
def maxProfit(self, prices):
	"""
	:type prices: List[int]
	:rtype: int
	"""
	profit=0
	for i in range(len(prices)-1):
		if prices[i+1] > prices[i]:
			profit+=prices[i+1]-prices[i]
	
	return profit