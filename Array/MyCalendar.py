#Source : https://leetcode.com/problems/my-calendar-i/
#Author : Yuan Wang
#Date   : 2019-05-25
'''
********************************************************************************** 
Implement a MyCalendar class to store your events. A new event can be added if 
adding the event will not cause a double booking.

Your class will have the method, book(int start, int end). Formally, this represents
 a booking on the half open interval [start, end), the range of real numbers x such 
 that start <= x < end.

A double booking happens when two events have some non-empty intersection (ie., there
 is some time that is common to both events.)

For each call to the method MyCalendar.book, return true if the event can be added to
 the calendar successfully without causing a double booking. Otherwise, return false 
 and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.
book(start, end)
Example 1:

MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false
MyCalendar.book(20, 30); // returns true
Explanation: 
The first event can be booked.  The second can't because time 15 is already booked
 by another event.
The third event can be booked, as the first event takes every time less than 20, 
but not including 20.
**********************************************************************************/
'''
import bisect
#My solution,Time complexity:O(n^2)
class MyCalendar:

    def __init__(self):
        self.calendar = {}

    def book(self, start: int, end: int) -> bool:
        if start not in self.calendar:
            for key in self.calendar:
                if key <= start <= self.calendar[key]:
                    return False
                elif key <= end-1 <= self.calendar[key]:
                    return False
                elif start <= key <= self.calendar[key] <= end-1:
                    return False
            self.calendar[start] = end-1
            return True
        else:
            return False

#Other solution, Time complexity:O(nlogn)
class MyCalendar:

    def __init__(self):
        self.book_list = []

    def book(self, start: 'int', end: 'int') -> 'bool':
        i = bisect.bisect_right(self.book_list,start)
        if i%2!=0:
            return False
        j = bisect.bisect_left(self.book_list,end)
        if i!=j:
            return False
        self.book_list[i:i] = [start,end]
        return True

#My solution based on Java TreeMap
class MyCalendar:

    def __init__(self):
        self.start = []
        self.end = []

    def book(self, start: int, end: int) -> bool:

        ceillingKey = bisect.bisect_left(self.start,start)
        if ceillingKey != len(self.start) and self.start[ceillingKey] < end:
            return False
        floorKey = ceillingKey-1
        if floorKey >= 0 and self.end[floorKey] > start:
            return False
        bisect.insort(self.start,start)
        bisect.insort(self.end,end)
        return True