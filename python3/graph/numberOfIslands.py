"""
    200 - Number of Islands - Medium
    https://leetcode.com/problems/number-of-islands/
    Topics: Graph, DFS

    Run complexity: O(M * N)
    Space complexity: O(n)
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(i, j):
            if (
                i < 0 or
                j < 0 or
                i == rows or
                j == cols or
                grid[i][j] != '1'
            ):
                return 
            
            grid[i][j] = '#'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    dfs(i, j)     
                    islands += 1
        return islands       

