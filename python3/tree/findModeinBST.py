"""
    501 - Find Mode in Binary Search Tree - Easy
    https://leetcode.com/problems/find-mode-in-binary-search-tree/
    Topics: Binary Search Tree

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
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count_dict = defaultdict(int)
        max_count = 0
        res = []

        def helper(node):
            if not node:
                return
                
            count_dict[node.val] += 1
            helper(node.left)
            helper(node.right)  
            
        helper(root)
        for key, val in count_dict.items():
            if val > max_count:
                res.clear()
                max_count = val
                res.append(key)
            elif val == max_count:
                res.append(key)
                
        return res
            