'''
Source : https://leetcode.com/problems/validate-binary-search-tree/
Author : Yuan Wang
Date   : 2018-06-21

/********************************************************************************** 
*Given a binary tree, determine if it is a valid binary search tree (BST).
*
*Assume a BST is defined as follows:
*
*The left subtree of a node contains only nodes with keys less than the node's key.
*The right subtree of a node contains only nodes with keys greater than the node's key.
*Both the left and right subtrees must also be binary search trees.
*Example 1:
*
*Input:
*	2
*   / \
*  1   3
*Output: true
*Example 2:
*
*	5
*   / \
*  1   4
*	 / \
*	3   6
*Output: false
*Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
*	 is 5 but its right child's value is 4.
**********************************************************************************/
'''

# Definition for a binary tree node.
# class TreeNode:
#	 def __init__(self, x):
#	 self.val = x
#	 self.left = None
#	 self.right = None

#Inorder traverse, if this is a binary search tree, then the list should be Non-decreasing
#Time Complexity:O(n), Space Complexity:O(n)
def isValidBST(self, root):
	output = []
	self.inOrder(root, output)
	
	for i in range(1, len(output)):
		if output[i-1] >= output[i]:
			return False

	return True

def inOrder(self, root, output):
	if root is None:
		return
	
	self.inOrder(root.left, output)
	output.append(root.val)
	self.inOrder(root.right, output)

def isValidBST(self, root, lessThan = float('inf'), largerThan = float('-inf')):
	if not root:
		return True
	if root.val <= largerThan or root.val >= lessThan:
		return False
	return self.isValidBST(root.left, min(lessThan, root.val), largerThan) and self.isValidBST(root.right, lessThan, max(root.val, largerThan))

