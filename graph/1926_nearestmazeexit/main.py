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

# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/description
class Solution:

    class Solution:
    def bfs(self, maze, entrance):
        n = len(maze)
        m = len(maze[0])
        DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1)]
        queue = deque([(entrance[0], entrance[1], 0)])
        while queue:
            i, j, count = queue.popleft()
            if (i == 0 or j == 0 or i == n - 1 or j == m - 1) and (i != entrance[0] or j != entrance[1]):
                return count
            for drct in DIRECTIONS:
                di, dj = i + drct[0], j + drct[1]
                if 0 <= di < n and 0 <= dj < m and maze[di][dj] == '.':
                    maze[di][dj] = '+'
                    queue.append((di, dj, count + 1))
        return -1 

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        return self.bfs(maze, entrance)

            
   
