'''
Source : https://leetcode.com/problems/binary-tree-inorder-traversal/
Author : Yuan Wang
Date   : 2018-07-30

/********************************************************************************** 
*Given a binary tree, return the inorder traversal of its nodes' values.
*
*Example:
*
*Input: [1,null,2,3]
*   1
*	\
*	 2
*	/
*   3
*
*Output: [1,3,2]
**********************************************************************************/
'''

# Definition for a binary tree node.
# class TreeNode:
#	 def __init__(self, x):
#	 self.val = x
#	 self.left = None
#	 self.right = None

#Recursive solution,Time complexity:O(n) Space complexity:O(n)
def inorderTraversal(self, root):
	"""
	:type root: TreeNode
	:rtype: List[int]
	"""
	
	return self.printInorder(root,[])
	
def printInorder(self,root,lst):
	if root:
		self.printInorder(root.left,lst)
		lst.append(root.val)
		self.printInorder(root.right,lst)
	return lst

#Iteratively solution, Time complexity:O(n) Space complexity:O(n)
def inorderTraversal(self,root):
	res,stack=[],[]
	while True:
		while root:
			stack.append(root)
			root=root.left
		if not stack:
			return res
		node=stack.pop()
		res.append(node.val)
		root=node.right
