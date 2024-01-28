"""
    1379 - Find a Corresponding Node of a Binary Tree in a Clone of That Tree - Easy
    https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
    Topics: Binary Search Tree, DFS

    Runtime complexity: O(n)
    Spacetime complexity: O(1)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        res = TreeNode()

        def inorder(original, cloned, target):
            if not original and not cloned:
                return

            inorder(original.left, cloned.left, target)

            nonlocal res
            if target == original:
                res = cloned
            
            inorder(original.right, cloned.right, target)
        
        inorder(original, cloned, target)
        return res
