'''
Source : https://leetcode.com/problems/long-pressed-name/description/
Author : Yuan Wang
Date   : 2019-01-12

/********************************************************************************** 
*Your friend is typing his name into a keyboard.  Sometimes, when typing a character
*c, the key might get long pressed, and the character will be typed 1 or more times.
*
*You examine the typed characters of the keyboard.  Return True if it is possible that
*it was your friends name, with some characters (possibly none) being long pressed.
*
*Example 1:
*
*Input: name = "alex", typed = "aaleex"
*Output: true
*Explanation: 'a' and 'e' in 'alex' were long pressed.
*Example 2:
*
*Input: name = "saeed", typed = "ssaaedd"
*Output: false
*Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
**********************************************************************************/
'''

def isLongPressedName(name, typed):
        g1 = [(k, len(list(grp))) for k, grp in itertools.groupby(name)]
        g2 = [(k, len(list(grp))) for k, grp in itertools.groupby(typed)]
        if len(g1) != len(g2):
            return False

        return all(k1 == k2 and v1 <= v2
                   for (k1,v1), (k2,v2) in zip(g1, g2))