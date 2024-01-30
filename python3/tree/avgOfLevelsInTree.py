"""
    637 - Average of Levels in Binary Tree - Easy
    https://leetcode.com/problems/average-of-levels-in-binary-tree/
    Topics: Tree

    Runtime complexity: O(n^2)
    Spacetime complexity: O(n)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue, res = [root], [],
        
        while queue:
            queue_len, row = len(queue), 0

            for i in range(queue_len):
                curr = queue.pop(0)
                row += curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(row/queue_len)
            
        return res