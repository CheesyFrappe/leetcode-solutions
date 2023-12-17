"""
    145 - Binary Tree Postorder Traversal - Easy
    https://leetcode.com/problems/binary-tree-postorder-traversal/
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

# Recursive Solution
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def postorder(root):
            if root:
                postorder(root.left)
                postorder(root.right)
                res.append(root.val)

        postorder(root)
        return res

"""
Iterative solution:
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return

        stack = [root]
        res = []

        while stack:
            root = stack.pop()
            res.append(root.val)

            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        return res[::-1]
"""