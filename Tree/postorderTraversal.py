'''
Source : https://leetcode.com/problems/binary-tree-postorder-traversal/
Author : Yuan Wang
Date   : 2018-08-02

/********************************************************************************** 
*Given a binary tree, return the postorder traversal of its nodes' values.
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
*Output: [3,2,1]
**********************************************************************************/
'''

# Definition for a binary tree node.
# class TreeNode:
#	 def __init__(self, x):
#	 self.val = x
#	 self.left = None
#	 self.right = None

#Self solution using recursive
def postorderTraversal(self, root):
	"""
	:type root: TreeNode
	:rtype: List[int]
	"""
	return self.printpostorder(root,[])
	
def printpostorder(self,root,lst):
	if root:
		self.printpostorder(root.left,lst)
		self.printpostorder(root.right,lst)
		lst.append(root.val)
	return lst

#Other solution using iterative
def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        stack = []
        curr = root
        while True:
            if curr:
                if curr.right:
                    stack.append(curr.right)
                stack.append(curr)
                curr = curr.left
                continue
            if not stack:
                break
            node = stack.pop()
            if node.right and stack and node.right == stack[-1]:
                curr = stack.pop()
                stack.append(node)
            else:
                ret.append(node.val)
        return ret