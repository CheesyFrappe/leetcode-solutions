"""
    1557 - Minimum Number of Vertices to Reach All Nodes - Medium
    https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/
    Topics: Graph

    Time complexity: O(n)
    Space complexity: O(n)
"""

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        bit_vector = [0] * n
        res = []

        for u,v in edges:
            bit_vector[v] = 1

        for i in range(n):
            if bit_vector[i] == 0:
                res.append(i) 
        return res
