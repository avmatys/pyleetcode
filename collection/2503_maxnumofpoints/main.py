from typing import List
from datetime import datetime
from heapq import heappop, heappush

# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper

# https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/description/
class Solution:

    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1)]
        m, n = len(grid), len(grid[0])
        sorted_queries = sorted([(val, i) for i, val in enumerate(queries)])
        answers = [0] * len(queries)
        queue = []
        heappush(queue, (grid[0][0], 0, 0))
        points = 0
        for query_val, query_idx in sorted_queries:
            while queue:
                if queue[0][0] >= query_val:
                    break
                qk, i, j = heappop(queue)
                if grid[i][j] != -1:
                    points += 1
                    for off_i, off_j in DIRECTIONS:
                        ni, nj = i + off_i, j + off_j
                        if 0 <= ni < m and 0 <= nj < n:
                            heappush(queue, (grid[ni][nj], ni, nj))
                    grid[i][j] = -1
            answers[query_idx] = points
        return answers


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([[1,2,3],[2,5,7],[3,5,1]], [5,6,2]), [5,8,1])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.maxPoints(*input), expected)

    
   
