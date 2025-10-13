from typing import List

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        # Adj list
        adj = [[] for _ in range(n)]
        for s, e in edges:
            adj[s].append(e)
        # Calc indegree
        indegree = [0] * n
        for v in range(n):
            for u in adj[v]:
                indegree[u] += 1
        # Traverse the graph
        dp = [[0 for _ in range(26)] for _ in range(n)]
        gpath = []
        res = 0
        q = deque(v for v in range(n) if indegree[v] == 0)
        while q:
            v = q.popleft()
            dp[v][ord(colors[v]) - ord('a')] += 1
            gpath.append(v)
            res = max(res, max(dp[v]))
            for u in adj[v]:
                indegree[u] -= 1
                for i in range(26):
                    dp[u][i] = max(dp[u][i], dp[v][i])
                if indegree[u] == 0:
                    q.append(u)

        # Check cycle
        if len(gpath) != n:
            return -1

        return res
