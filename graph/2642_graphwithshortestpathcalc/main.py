from typing import List

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = [[] for _ in range(n)]
        self.n = n
        # Add edges to the graph
        for e in edges:
            self.addEdge(e)

    def addEdge(self, edge: List[int]) -> None:
        # Guaranteed that graph doesn't have this edge
        start, end, cost = edge
        self.graph[start].append((end, cost))

    def shortestPath(self, node1: int, node2: int) -> int:
        q = [(0, node1)] # Use pq for the dejkstra
        costs = [float('inf')] * self.n
        costs[node1] = 0 # Start point
        while q:
            curr_cost, curr_node = heapq.heappop(q)
            if curr_cost > costs[curr_node]:
                continue # Worst path
            if curr_node == node2:
                return curr_cost
            for next_node, next_cost in self.graph[curr_node]:
                if costs[next_node] < curr_cost + next_cost:
                    continue # Existing path is better
                costs[next_node] = curr_cost + next_cost
                heapq.heappush(q, (costs[next_node], next_node))
        return -1



# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
