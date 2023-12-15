"""
    94 - Binary Tree Inorder Traversal - Easy
    https://leetcode.com/problems/binary-tree-inorder-traversal
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

# Recursive solution:
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(node):

            if node:
                inorder(node.left)
                res.append(node.val)
                inorder(node.right)

        inorder(root)
        return res



"""
Iterative solution:

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
            res = []
            stack = []

            # loop until either current node is not None or the stack is not empty
            while root or stack:

                # travers to the leftmost node and push each encountered node onto the stack
                while root:
                    stack.append(root)
                    root = root.left
                
                # pop the last node from the stack (most recently left-visited node)
                root = stack.pop()

                # append the value of the popped node to the result list
                res.append(root.val)

                # move to the right subtree to continue the in-order traversal
                root = root.right
            
        return res
"""

