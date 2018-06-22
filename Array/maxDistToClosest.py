'''
Source : https://leetcode.com/problems/maximize-distance-to-closest-person/
Author : Yuan Wang
Date   : 2018-06-22

/********************************************************************************** 
*In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 
*
*There is at least one empty seat, and at least one person sitting.
*
*Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 
*
*Return that maximum distance to closest person.
*
*Example 1:
*
*Input: [1,0,0,0,1,0,1]
*Output: 2
*Explanation: 
*If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
*If Alex sits in any other open seat, the closest person has distance 1.
*Thus, the maximum distance to the closest person is 2.
*Example 2:
*
*Input: [1,0,0,0]
*Output: 3
*Explanation: 
*If Alex sits in the last seat, the closest person is 3 seats away.
*This is the maximum distance possible, so the answer is 3.
**********************************************************************************/
'''

def maxDistToClosest(seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        
        people = (i for i, seat in enumerate(seats) if seat)
        prev, future = None, next(people)

        ans = 0
        for i, seat in enumerate(seats):
            if seat:
                prev = i
            else:
                while future is not None and future < i:
                    future = next(people, None)

                left = float('inf') if prev is None else i - prev
                right = float('inf') if future is None else future - i
                ans = max(ans, min(left, right))

        return ans


def maxDistToClosestB(seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        
        ans = 0
        for seat, group in itertools.groupby(seats):
            if not seat:
                K = len(list(group))
                ans = max(ans, (K+1)/2)
                
        return int(max(ans, seats.index(1), seats[::-1].index(1)))

