"""
    144 - Binary Tree Preorder Traversal - Easy
    https://leetcode.com/problems/binary-tree-preorder-traversal/
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

#Recursive solution:
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
            
        def preorder(node):
            if node:
                res.append(node.val)
                preorder(node.left)
                preorder(node.right)

        preorder(root)
        return res


"""
Iterative solution:

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []

        while root or stack:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            root = root.right

        return res
"""