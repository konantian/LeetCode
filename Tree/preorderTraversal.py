'''
Source : https://leetcode.com/problems/binary-tree-preorder-traversal/
Author : Yuan Wang
Date   : 2018-07-30

/********************************************************************************** 
*Given a binary tree, return the preorder traversal of its nodes' values.
*
*Example:
*
*Input: [1,null,2,3]
*   1
*	\
*	 2
*	/
*  3
*
*Output: [1,2,3]
**********************************************************************************/
'''

# Definition for a binary tree node.
# class TreeNode:
#	 def __init__(self, x):
#	 self.val = x
#	 self.left = None
#	 self.right = None

#Recursively
def preorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		return self.printPreorder(root,[])
	
def printPreorder(self,root,lst):
	if root:
		lst.append(root.val)
		self.printPreorder(root.left,lst)
		self.printPreorder(root.right,lst)
	
	return lst

#Iteratively
def preorderTraversal(self, root):
	"""
	:type root: TreeNode
	:rtype: List[int]
	"""
	# stack storing right nodes
	rightNodes = []
	
	result = []
	
	cur = root
	
	while cur:
		result.append(cur.val)
		if cur.right:
			rightNodes.append(cur.right)
	
		cur = cur.left
		if not cur and len(rightNodes)!= 0:
			cur = rightNodes.pop()
	
	
	return result	