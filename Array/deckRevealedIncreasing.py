'''
Source : https://leetcode.com/problems/reveal-cards-in-increasing-order/
Author : Yuan Wang
Date   : 2019-01-06

/********************************************************************************** 
*In a deck of cards, every card has a unique integer.  You can order the deck in any
*order you want.
*
*Initially, all the cards start face down (unrevealed) in one deck.
*
*Now, you do the following steps repeatedly, until all cards are revealed:
*
*Take the top card of the deck, reveal it, and take it out of the deck.
*If there are still cards in the deck, put the next top card of the deck at the bottom
*of the deck.
*If there are still unrevealed cards, go back to step 1.  Otherwise, stop.
*Return an ordering of the deck that would reveal the cards in increasing order.
*
*Example 1:
*
*
*Input: [17,13,11,2,3,5,7]
*Output: [2,13,3,11,5,17,7]
**********************************************************************************/
'''
import collections


#Time complexity:O(nlogn) Space complexity:O(n)
def deckRevealedIncreasing(deck):
    """
    :type deck: List[int]
    :rtype: List[int]
    """
    N = len(deck)
    index = collections.deque(range(N))
    ans = [None] * N

    for card in sorted(deck):
    	ans[index.popleft()] = card
    	if index:
    		index.append(index.popleft())
    return ans


import unittest
class Test(unittest.TestCase):

    def setUp(self):
        self.A = [17,13,11,2,3,5,7]

    def test(self):
        self.assertEqual(deckRevealedIncreasing(self.A), [2,13,3,11,5,17,7])


if __name__ == '__main__':
    unittest.main()