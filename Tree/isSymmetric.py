'''
Source : https://leetcode.com/problems/symmetric-tree/
Author : Yuan Wang
Date   : 2018-07-21

/********************************************************************************** 
*Given a binary tree, check whether it is a mirror of itself (ie, symmetric around 
*its center).
*
*For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
*
*	1
*   / \
*  2   2
* / \ / \
*3  4 4  3
*But the following [1,2,2,null,3,null,3] is not:
*	1
*   / \
*  2   2
*   \   \
*   3	3
**********************************************************************************/

Time complexity:O(n) Space complexity:O(1)
Two trees are a mirror reflection of each other if:
Their two roots have the same value.
The right subtree of each tree is a mirror reflection of the left subtree of the other tree.
'''

def isSymmetric(root):
	"""
	:type root: TreeNode
	:rtype: bool
	"""
	
	return isMirror(root,root)

def isMirror(rootA,rootB):
	if rootA and rootB:
		return rootA.val == rootB.val and isMirror(rootA.right,rootB.left) and isMirror(rootA.left,rootB.right)

	return rootA is rootB
