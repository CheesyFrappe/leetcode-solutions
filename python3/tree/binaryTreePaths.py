"""
    257 - Binary Tree Paths - Easy
    https://leetcode.com/problems/binary-tree-paths
    Topics: Tree

    Runtime complexity: O(n)
    Spacetime complexity: O(n)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        s = ""
        res = []

        def path(node, res, s):
            if not node:
                return

            if not node.left and not node.right:
                s += f"{node.val}"
                res.append(s)
                return
            
            s += f"{node.val}->"
            path(node.left, res, s)
            path(node.right, res, s)
                
        path(root, res, s)
        return res
