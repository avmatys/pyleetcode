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

# https://leetcode.com/problems/rotting-oranges/
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        m, n = len(grid), len(grid[0])
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
                elif grid[i][j] == 1:
                    fresh += 1
        # Start processing
        while queue:
            i, j, count = queue.popleft()
            for drct in [(1,0),(0,1),(-1,0),(0,-1)]:
                di, dj = i + drct[0], j + drct[1]
                if 0 <= di < m and 0 <=dj < n and grid[di][dj] == 1:
                    fresh -= 1
                    if fresh == 0:
                        return count + 1
                    grid[di][dj] = 2
                    queue.append((di,dj,count+1))
        return 0 if fresh == 0 else -1
             
    
   
