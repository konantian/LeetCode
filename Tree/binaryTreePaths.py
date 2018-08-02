'''
Source : https://leetcode.com/problems/binary-tree-paths/
Author : Yuan Wang
Date   : 2018-08-02

/********************************************************************************** 
*Given a binary tree, return all root-to-leaf paths.
*
*Note: A leaf is a node with no children.
*
*Example:
*
*Input:
*
*   1
* /   \
*2     3
* \
*  5
*
*Output: ["1->2->5", "1->3"]
*
*Explanation: All root-to-leaf paths are: 1->2->5, 1->3
**********************************************************************************/
'''

# Definition for a binary tree node.
# class TreeNode:
#	 def __init__(self, x):
#	 self.val = x
#	 self.left = None
#	 self.right = None

def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        
        result=self.findPath(root,[],"")
        return result
        
def findPath(self,root,result,temp):
        
        temp+=str(root.val)
        if root.left:
            self.findPath(root.left,result,temp+"->")
        if root.right:
            self.findPath(root.right,result,temp+"->")
        if not root.left and not root.right:
            result.append(temp)
                
        return result