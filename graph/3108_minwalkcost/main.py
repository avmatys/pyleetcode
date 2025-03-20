from typing import List
from datetime import datetime
from typing import Optional
from collections import deque

# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper

# https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/description/
class Solution:

    # Calc cost and mark nodes to the component_idx
    def dfs(self, adj_list, node, visited, components, component_idx):
        visited.add(node)
        components[node] = component_idx
        cost = -1
        for neighbour, weight in adj_list[node]:
            cost &= weight
            if neighbour not in visited:
                cost &= self.dfs(adj_list, neighbour, visited, components, component_idx)
        return cost

    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        # Build an adj list
        adj_list = [[] for _ in range(n)]
        for u, v, w in edges:
            adj_list[u].append((v,w))
            adj_list[v].append((u,w))
        # Go through the each node connected components and calc cost
        visited = set()
        components = [-1] * n
        costs = []
        component_idx = 0
        for node in range(n):
            if node not in visited:
                # In order to get the min price we should go and do bitwise and 
                # for all nodes in the graph
                cost = self.dfs(adj_list, node, visited, components, component_idx)
                costs.append(cost)
                component_idx += 1
        # Process the inbound queris
        result = []
        for s,e in query:
            if components[s] == components[e]:
                result.append(costs[components[s]])
            else:
                result.append(-1)
        return result
