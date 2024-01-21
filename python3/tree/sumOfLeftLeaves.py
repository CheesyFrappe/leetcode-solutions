"""
    404 - Sum of Left Leaves - Easy
    https://leetcode.com/problems/sum-of-left-leaves/
    Topics: Binary Tree, Depth-First-Search, Breadth-First-Search

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
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # if left node exits and it's a leaf node, add it
        #  and check right sub-tree
        if root.left and not root.left.left and not root.left.right:    
            return root.left.val + self.sumOfLeftLeaves(root.right)

        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        