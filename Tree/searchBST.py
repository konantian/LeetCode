'''
Source : https://leetcode.com/problems/search-in-a-binary-search-tree/
Author : Yuan Wang
Date   : 2021-01-17

/********************************************************************************** 
*You are given the root of a binary search tree (BST) and an integer val.
*Find the node in the BST that the node's value equals val and return the subtree 
*rooted with that node. If such a node does not exist, return null.
*
*Example:
*
*Input: [4,2,7,1,3], val = 2
*Output: [2,1,3]
**********************************************************************************/
'''

# Time complexity: O(logn) Space Complexity : O(logn)
def searchBST(root: TreeNode, val: int) -> TreeNode:
    if not root:
        return None
    if root.val == val:
        return root
    if val > root.val:
        return searchBST(root.right,val)
    else:
        return searchBST(root.left, val)