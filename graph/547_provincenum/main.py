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

# https://leetcode.com/problems/number-of-provinces/description
class Solution:

    @timeit
    def dfs(self, node, matrix, visited):
        visited[node] = 1
        queue = deque([node])
        while queue:
            i = queue.popleft()
            for j in range(len(matrix)):
                if matrix[i][j] == 1 and not visited[j]:
                    queue.append(j)
                    visited[j] = 1

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        count = 0
        visited = [0] * n
        for i in range(n):
            if not visited[i]:
                count += 1
                self.dfs(i, isConnected, visited)
        return count  

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([[1,1,0],[1,1,0],[0,0,1]], 2)
    ]
    for case in cases:
        expected = case[1]
        result = solution.findCircleNum(case[0])
        judge(result, expected)
    
   
