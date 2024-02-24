"""
    2642 - Design Graph With Shortest Path Calculator - Hard
    https://leetcode.com/problems/design-graph-with-shortest-path-calculator/
    Topics: Graph, Shortest

    Time complexity: O((V * E) * log(V))
    Space complexity: O(V)
"""

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.nodes = n
        self.graph = defaultdict(list)
        for edge in edges:
            self.graph[edge[0]].append([edge[1], edge[2]])

    def addEdge(self, edge: List[int]) -> None:
        self.graph[edge[0]].append([edge[1], edge[2]])

    def shortestPath(self, node1: int, node2: int) -> int:
        distances = {node: float('inf') for node in range(self.nodes)}
        distances[node1] = 0

        heap = [(0, node1)]
        while heap:
            curr_dist, curr_node = heapq.heappop(heap)

            if distances[curr_node] < curr_dist:
                continue    
            
            for neighbour, weight in self.graph[curr_node]:
                dist = curr_dist + weight

                if dist < distances[neighbour]:
                    distances[neighbour] = dist
                    heapq.heappush(heap, (dist, neighbour))
        
        return distances[node2] if distances[node2] != float('inf') else -1

