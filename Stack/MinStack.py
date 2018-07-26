#Source : https://leetcode.com/problems/min-stack/
#Author : Yuan Wang
#Date   : 2018-07-26
'''
********************************************************************************** 
*Design a stack that supports push, pop, top, and retrieving the minimum element in
*constant time.
*
*push(x) -- Push element x onto stack.
*pop() -- Removes the element on top of the stack.
*top() -- Get the top element.
*getMin() -- Retrieve the minimum element in the stack.
*Example:
*MinStack minStack = new MinStack();
*minStack.push(-2);
*minStack.push(0);
*minStack.push(-3);
*minStack.getMin();   --> Returns -3.
*minStack.pop();
*minStack.top();	  --> Returns 0.
*minStack.getMin();   --> Returns -2.
**********************************************************************************/
'''

class MinStack:

	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self.__items=[]
		self.mim=None
	

	def push(self, x):
		"""
		:type x: int
		:rtype: void
		"""
		if not self.__items:
			self.mim=x
		else:
			self.mim = x if x < self.mim else self.mim
		
		self.__items.append(x)
	

	def pop(self):
		"""
		:rtype: void
		"""
		element=self.__items.pop()
		if element == self.mim:
			if len(self.__items) != 0:
				self.mim=min(self.__items)
			else:
				self.mim=None
		return element

	def top(self):
		"""
		:rtype: int
		"""
		return self.__items[len(self.__items)-1]

	def getMin(self):
		"""
		:rtype: int
		"""
		return self.mim
