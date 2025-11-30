from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        q = deque()
        q.append((0,0))
        res = 0
        while q:
            k = len(q)
            res += 1
            for _ in range(k):
                i, j = q.popleft()
                if grid[i][j] == 1:
                    continue
                if i == m - 1 and j == n - 1:
                    return res
                grid[i][j] = 1 # mark as visited
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if ni < 0 or ni >= m: continue
                    if nj < 0 or nj >= n: continue
                    if grid[ni][nj] == 1: continue
                    q.append((ni, nj))
        return -1
