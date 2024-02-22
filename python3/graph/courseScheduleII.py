"""
    210 - Course Schedule II - Medium
    https://leetcode.com/problems/course-schedule-ii/
    Topics: Graph, DFS

    Run complexity: O(M * N)
    Space complexity: O(M * N)
"""

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = [[] for x in range(numCourses)]
        inDegree = [0] * numCourses
        queue = []

        # p[1] -> p[0]
        # build adjaceny list and incoming nodes per node
        for p in prerequisites:
            adj_list[p[1]].append(p[0])
            inDegree[p[0]] += 1
        
        # take a node with no incoming node as root
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)

        res = []
        # traverse the graph and keep track of the courses
        while queue:
            node = queue.pop(0)
            res.append(node)

            for adj_node in adj_list[node]:
                inDegree[adj_node] -= 1
                if inDegree[adj_node] == 0:
                    queue.append(adj_node)
        
        return [] if len(res) != numCourses else res
