class Solution:
    def topologicalSort(self, graph, n, in_degree):
        queue = []
        order = []

        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)
        
        while queue:
            curr_node = queue.pop(0)
            order.append(curr_node)

            for adj_node in graph[curr_node]:
                in_degree[adj_node] -= 1
                if in_degree[adj_node] == 0:
                    queue.append(adj_node)
        return order

    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        item_in_degree = [0] * n
        item_graph = defaultdict(list)
        group_graph = defaultdict(list)

        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
        
        for i in range(n):
            for node in beforeItems[i]:
                if group[node] == group[i]:
                    item_graph[node].append(i)
                    item_in_degree[i] += 1
        
        group_in_degree = [0] * (m + 1)
        sorted_items_per_group = defaultdict(list)

        item_order = self.topologicalSort(item_graph, n, item_in_degree)
        for u in item_order:
            sorted_items_per_group[group[u]].append(u)    
        
        for i in range(n):
            for node in beforeItems[i]:
                if group[node] != group[i]:
                    group_graph[group[node]].append(group[i])
                    group_in_degree[group[i]] += 1
        
        group_order = self.topologicalSort(group_graph, m+1, group_in_degree)

        ans = []
        for group in group_order:
            ans.extend(sorted_items_per_group[group])
        
        return ans if len(ans) == n else []
