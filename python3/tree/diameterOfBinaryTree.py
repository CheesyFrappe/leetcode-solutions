"""
    543 - Diameter of Binary Tree - Easy
    https://leetcode.com/problems/diameter-of-binary-tree/
    Topics: Binary Search Tree, DFS

    Runtime complexity: O(n)
    Spacetime complexity: O(1)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def inorder(node):
            if not node:
                return 0

            left = inorder(node.left)
            right = inorder(node.right)

            nonlocal res
            res = max(left + right, res)

            return 1 + max(left, right)
        
        inorder(root)
        return res
