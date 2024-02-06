"""
    653 - Two Sum IV - Input is a BST - Easy
    https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
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
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        bucket = []

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            
            nonlocal bucket
            bucket.append(node.val)
            
            inorder(node.right)
        
        inorder(root)
        left_p = 0
        right_p = len(bucket) - 1
        
        while left_p < right_p:
            sum_vals = bucket[left_p] + bucket[right_p]

            if sum_vals == k:
                return True
            elif sum_vals < k:
                left_p += 1
            else:
                right_p -= 1

        return False  
