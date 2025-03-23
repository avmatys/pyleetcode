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


# https://leetcode.com/problems/number-of-ways-to-arrive-at-destination
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        graph = [[] for _ in range(n)]
        for u,v,w in roads:
            graph[u].append((v,w))
            graph[v].append((u,w))
        dist = [[float('inf'), 0] for _ in range(n)] # distance, paths count
        dist[0] = [0,1]
        minheap = [(0,0)] # dist, vertex
        while minheap:
            u_dist, u = heappop(minheap)
            if u_dist > dist[u][0]:
                continue
            for v, w in graph[u]:
                v_dist = u_dist + w
                if v_dist == dist[v][0]: # Found the same path
                    dist[v][1] = (dist[v][1] + dist[u][1]) % MOD
                elif v_dist < dist[v][0]: # Found a better path
                    dist[v][0] = v_dist
                    dist[v][1] = dist[u][1]
                    heappush(minheap, (v_dist, v))
        return dist[n-1][1]
