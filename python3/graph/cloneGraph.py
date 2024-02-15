"""
    133 - Clone Graph - Medium
    https://leetcode.com/problems/clone-graph/
    Topics: Graph, DFS, BFS, Hash Table

    Time complexity: O(V + E)
    Space complexity: O(V)
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        org_to_clone = {}

        def dfs(node):
            if node in org_to_clone:
                return org_to_clone[node]
            
            copy_node = Node(node.val)
            org_to_clone[node] = copy_node

            for neighbour in node.neighbors:
                copy_node.neighbors.append(dfs(neighbour))
            return copy_node
        return dfs(node) if node else None