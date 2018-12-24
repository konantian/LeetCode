'''
Source : https://leetcode.com/problems/min-cost-climbing-stairs/
Author : Yuan Wang
Date   : 2018-12-24

/********************************************************************************** 
*On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
*
*Once you pay the cost, you can either climb one or two steps. You need to find minimum
*cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.
*
*Example 1:
*Input: cost = [10, 15, 20]
*Output: 15
*Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
*Example 2:
*Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
*Output: 6
*Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
**********************************************************************************/
'''

import unittest
#Solution 1 using DP,time complexity:O(n), space complexity:O(1)
def minCostClimbingStairsA(cost):
    """
    :type cost: List[int]
    :rtype: int
    """
    f1=f2=0
    for x in reversed(cost):
        f1,f2=x+min(f1,f2),f1
    return min(f1,f2)


#Solution 1, using greedy, time complexity:O(n), space complexity:O(1)
def minCostClimbingStairsB(cost):
    """
    :type cost: List[int]
    :rtype: int
    """
    cost.append(0)
    for i in range(2,len(cost)):
        cost[i] += min(cost[i-1], cost[i-2])
    return cost[-1]


class Test(unittest.TestCase):

    def setUp(self):
        self.cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

    def test_A(self):
        self.assertEqual(minCostClimbingStairsA(self.cost), 6)

    def test_B(self):
        self.assertEqual(minCostClimbingStairsB(self.cost), 6)

if __name__ == '__main__':
    unittest.main()
