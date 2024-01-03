"""
    222 - Count Complete Tree Nodes - Easy
    https://leetcode.com/problems/count-complete-tree-nodes
    Topics: Tree

    Runtime complexity: O((log2n)2)
    Spacetime complexity: O(1)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        height = self.calculateHeight(root)
        count = 0

        while root:
            if self.calculateHeight(root.right) == height - 1:
                count += pow(2, height)
                root = root.right
            else:
                count += pow(2, height - 1)
                root = root.left
            height -= 1
        return count


    def calculateHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1

        height = 0
        while root.left:
            root = root.left
            height += 1
        return height