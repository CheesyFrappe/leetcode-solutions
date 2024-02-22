"""
    797 - All Paths From Source to Target - Medium
    https://leetcode.com/problems/all-paths-from-source-to-target/
    Topics: Graph

    Time complexity: O(V * E) = O(n^2)
    Space complexity: O(n)
"""

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        temp_path = []

        def dfs(node):
            if node == len(graph) - 1:
                res.append(temp_path.copy())
                return 

            for adj_node in graph[node]:
                temp_path.append(adj_node)
                dfs(adj_node)
                temp_path.pop()
        
        temp_path.append(0)
        dfs(0)
        return res
                
