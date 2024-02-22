"""
    128 - Longest Consecutive Sequence - Medium
    https://leetcode.com/problems/longest-consecutive-sequence
    Topics: Array

    Runtime complexity: O(n)
    Spacetime complexity: O(M * N)
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        graph = {}
        visited = set()

        # build the graph
        for num in nums:
            graph[num] = graph.get(num, [])
            if num + 1 in graph:
                graph[num].append(num + 1)                
                graph[num + 1].append(num)
            if num - 1 in graph:
                graph[num].append(num - 1)                
                graph[num - 1].append(num)

        # traverse the graph        
        def dfs(node):
            if node in visited:
                return 0
            
            count = 1
            visited.add(node)
            for neighbour in graph[node]:
                count += dfs(neighbour)
            return count
        
        res = 0
        for node in graph:
            if node not in visited:
                res = max(res, dfs(node))
        return res
