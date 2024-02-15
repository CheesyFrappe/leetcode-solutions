"""
    207 - Course Schedule - Easy
    https://leetcode.com/problems/course-schedule/
    Topics: Graph

    Time complexity: O(V + E)
    Space complexity: O(V + E)
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for x in range(numCourses)]
        queue = []
        visited = 0

        # create a list holds every node and it adjacent nodes
        # and keep the count of pointed edges to a node
        for p in prerequisites:
            adj[p[1]].append(p[0])
            indegree[p[0]] += 1
        
        # take the root
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.pop(0)
            visited += 1

            for adj_node in adj[node]:
                indegree[adj_node] -= 1
                if indegree[adj_node] == 0:
                    queue.append(adj_node)
        return numCourses == visited
