"""
    102 - Binary Tree Level Order Traversal - Medium
    https://leetcode.com/problems/binary-tree-level-order-traversal
    Topics: Tree, BFS

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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        res = [[root.val]]
        temp = []

        while queue:
            node = queue.pop(0)
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
            
            if not queue:
                if temp:
                    res.append([n.val for n in temp])
                queue = temp
                temp = []

        return res