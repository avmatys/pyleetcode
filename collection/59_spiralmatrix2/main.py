from typing import List
from datetime import datetime
import heapq


# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper


# https://leetcode.com/problems/spiral-matrix-ii/description
class Solution:

    @timeit
    def generateMatrix(self, n: int) -> List[List[int]]:
        spiral = [[-1 for _ in range(n)] for _ in range(n)]
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        curr_dir = 0
        value = 0
        row, col = 0, -1 
        while value < n * n:
            next_row, next_col = row + directions[curr_dir][0], col + directions[curr_dir][1]
            if next_row >= n or next_col >= n or spiral[next_row][next_col] > 0:
                curr_dir = curr_dir + 1 if curr_dir < 3 else 0
                continue
            value += 1
            spiral[next_row][next_col] = value
            row, col = next_row, next_col
        return spiral


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ((3), [[1,2,3],[8,9,4],[7,6,5]]),
        ((1), [[1]]),
        ((4), [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.generateMatrix(input), expected)


    
   