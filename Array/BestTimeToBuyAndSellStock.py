'''
Source : https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock/
Author : Yuan Wang
Date   : 2018-06-02

/********************************************************************************** 
* 
* Say you have an array for which the ith element is the price of a given stock on day i.
* 
* If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), 
* design an algorithm to find the maximum profit.
*	   
**********************************************************************************/
'''

def maxProfit(prices):
	"""
	:type prices: List[int]
	:rtype: int
	"""
	max_profit, min_price = 0, float('inf')
	for price in prices:
		min_price = min(min_price, price)
		profit = price - min_price
		max_profit = max(max_profit, profit)
	return max_profit

def maxProfitB(prices):
	"""
	:type prices: List[int]
	:rtype: int
	"""
	maxCur=0
	maxSoFar=0
	for i in range(1,len(prices)):
		maxCur+=prices[i]-prices[i-1]
		maxCur=max(0,maxCur)
		maxSoFar=max(maxCur,maxSoFar)
	return maxSoFar
print(maxProfitB([7,1,5,3,6,4]))