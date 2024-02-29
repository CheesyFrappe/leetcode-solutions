"""
    1609 - Even Odd Tree - Medium
    https://leetcode.com/problems/even-odd-tree/
    Topics: BFS, Tree

    Time complexity: O(n)
    Space complexity: O(n)
"""


# Definition for a binary tree node.t
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root, None]
        level = 0

        while queue:
            curr_node = queue.pop(0)

            if not curr_node:
                level += 1
                queue.append(None)
                
                if not queue[0]:
                    break
                continue
            else:
                if level % 2 == 0 and curr_node.val % 2 == 0:
                    return False
                if level % 2 == 1 and curr_node.val % 2 == 1:
                    return False
            
            if level % 2 == 0 and queue[0]:
                if (curr_node.val >= queue[0].val):
                    return False

            if level % 2 == 1 and queue[0]:
                if (curr_node.val <= queue[0].val):
                    return False

            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
        
        return True
