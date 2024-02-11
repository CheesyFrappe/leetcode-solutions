"""
    1791 - Find Center of Star Graph - Easy
    https://leetcode.com/problems/find-center-of-star-graph/
    Topics: Graph

    Runtime complexity: O(1)
    Spacetime complexity: O(1)
"""

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        x, y = edges[0][0], edges[0][1]
        if x in edges[1]:
            return x
        if y in edges[1]:
            return y
        
        return -1