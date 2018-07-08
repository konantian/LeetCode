
#Source : https://leetcode.com/problems/excel-sheet-column-number/
#Author : Yuan Wang
#Date   : 2018-06-29
'''
********************************************************************************** 
*Initially, there is a Robot at position (0, 0). Given a sequence of its moves, 
*judge if this robot makes a circle, which means it moves back to the original place.
*
*The move sequence is represented by a string. And each move is represent by a 
*character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). 
*The output should be true or false representing whether the robot makes a circle.
*
*Example 1:
*Input: "UD"
*Output: true
*Example 2:
*Input: "LL"
*Output: false
**********************************************************************************/
'''

def judgeCircle(moves):
	"""
	:type moves: str
	:rtype: bool
	"""
	return moves.count("L") == moves.count("R") and moves.count("U") == moves.count("D")

moves="UDLR"
print(judgeCircle(moves))