'''
Source : https://leetcode.com/problems/balanced-binary-tree/
Author : Yuan Wang
Date   : 2018-07-21

/********************************************************************************** 
*Given a binary tree, determine if it is height-balanced.
*
*For this problem, a height-balanced binary tree is defined as:
*
*a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
*
*Example 1:
*
*Given the following tree [3,9,20,null,null,15,7]:
*
*	3
*   / \
*  9  20
*	/  \
*   15   7
*Return true.
*
*Example 2:
*
*Given the following tree [1,2,2,3,3,null,null,4,4]:
*
*	   1
*	  / \
*	 2   2
*	/ \
*   3   3
*  / \
* 4   4
*Return false.
**********************************************************************************/
'''

#Self solution, Time complexity:O(n^2) Space complexity:O(1)
def isBalanced(self, root):
	"""
	:type root: TreeNode
	:rtype: bool
	"""
	if root:
		left_depth=self.calDepth(root.left,0)
		right_depth=self.calDepth(root.right,0)
	
		if abs(left_depth-right_depth) > 1:
			return False
		else:
			return self.isBalanced(root.left) and self.isBalanced(root.right)
	else:
	
		return True
	
def calDepth(self,root,depth):
	if root:
		depth+=1
		return max(self.calDepth(root.left,depth),self.calDepth(root.right,depth))
	
	return depth

#Other solution,bottom up, Time complexity:O(n) Space complexity:O(1)
def isBalanced(self, root):
	"""
	:type root: TreeNode
	:rtype: bool
	"""
	return self.calDepth(root) != False
	
def calDepth(self,root):
	if not root:
		return True
	left=self.calDepth(root.left)
	if left == False:
		return False
	right=self.calDepth(root.right)
	if right == False:
		return False
	if abs(left-right) > 1:
		return False
	return max(left,right)+1