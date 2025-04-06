from typing import List
from datetime import datetime
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

# https://leetcode.com/problems/unique-paths-iii/
class Solution:

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # Prepare to the backgtacking
        m, n = len(grid), len(grid[0])
        total_count = m * n
        start_i, start_j = -1, -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == -1:
                    total_count -= 1
                if grid[i][j] == 1:
                    start_i, start_j = i, j
        # Build paths using backtrackin technique
        result = 0
        def build_path(curr_i, curr_j, remain_cnt):
            nonlocal result
            if  grid[curr_i][curr_j] == 2:
                result += int(remain_cnt == 0)
            else:
                tmp =  grid[curr_i][curr_j]
                grid[curr_i][curr_j] = -1
                for (offset_i, offset_j) in [(1,0),(-1,0),(0,1),(0,-1)]:
                    next_i = curr_i + offset_i
                    next_j = curr_j + offset_j
                    if 0 <= next_i < m and 0 <= next_j < n and grid[next_i][next_j] in {0, 2}:
                        build_path(next_i, next_j, remain_cnt - 1)
                grid[curr_i][curr_j] = tmp
        # Execute
        build_path(start_i, start_j, total_count - 1)
        return result
    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([[1,0,0,0],[0,0,0,0],[0,0,2,-1]], 2)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.uniquePathsIII(input), expected)

    
   
