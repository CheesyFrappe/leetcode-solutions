"""
    1971 - Find if Path Exists in Graph  - Easy
    https://leetcode.com/problems/find-if-path-exists-in-graph/
    Topics: Graph

    Time complexity: O(|V| + |E|)
    Space complexity: O(n + m)
"""
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = set()
        path_graph = defaultdict(list)

        for u, v in edges:
            path_graph[u].append(v)
            path_graph[v].append(u)
        
        def dfs(node, destination=destination):
            if node == destination:
                return True

            nonlocal visited, path_graph
            visited.add(node)

            for adjacent_node in path_graph[node]:
                if adjacent_node not in visited and dfs(adjacent_node):
                    return True

            return False

        return dfs(source)
