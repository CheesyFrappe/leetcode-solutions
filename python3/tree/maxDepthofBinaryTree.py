"""
    104 - Maximum Depth of Binary Tree - Easy
    https://leetcode.com/problems/maximum-depth-of-binary-tree
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = [root]
        temp = []
        res = 0

        while queue:
            node = queue.pop(0)

            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
            
            if not queue:
                res += 1
                queue = temp
                temp = []
        return res