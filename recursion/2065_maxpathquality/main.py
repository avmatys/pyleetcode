from typing import List

class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        n = len(values)
        graph = [[] for _ in range(n)]
        for s,e,t in edges:
            graph[s].append((e,t))
            graph[e].append((s,t))

        self.res = 0
        self.visited = [0] * n
        self.visited[0] = 1

        def dfs(node, t, score):
            if node == 0:
                self.res = max(self.res, score)
            for nxt, nt in graph[node]:
                if t + nt > maxTime:
                    continue
                nscore = score
                if self.visited[node] == 0:
                    nscore += values[node]
                self.visited[node] += 1
                dfs(nxt, t + nt, nscore)
                self.visited[node] -= 1

        dfs(0, 0, values[0])
        return self.res
