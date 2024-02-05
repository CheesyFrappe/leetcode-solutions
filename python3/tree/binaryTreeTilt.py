"""
    563 - Binary Tree Tilt - Easy
    https://leetcode.com/problems/binary-tree-tilt/
    Topics: Tree, Depth First Search

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
    def findTilt(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node):
            if not node:
                return 0
            
            if not node.left and not node.right:
                return node.val
            
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            nonlocal res
            res += abs(left_sum - right_sum)
            return left_sum + right_sum + node.val
                
        dfs(root)
        return res