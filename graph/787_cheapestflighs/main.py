from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for fr, to, price in flights:
            graph[fr].append((to, price))
        prices = [float('inf')] * n
        prices[src] = 0
        q = deque()
        q.append((src, 0, 0))
        while q:
            curr, cost, cnt = q.popleft()
            for nxt, ncost in graph[curr]:
                if prices[nxt] < cost + ncost: continue
                if cnt == k and nxt != dst: continue
                prices[nxt] = cost + ncost
                if cnt < k:
                    q.append((nxt, cost + ncost, cnt + 1))
        return prices[dst] if prices[dst] != float('inf') else -1

