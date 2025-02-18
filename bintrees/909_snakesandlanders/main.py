from typing import List
from datetime import datetime
from typing import Optional

# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper

# https://leetcode.com/problems/snakes-and-ladders/description
class Solution:

    @timeit
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        rolls_count = {1:0}
        queue =[1]
        for curr in queue:
            for i in range(curr + 1,min(curr + 7, n * n + 1)): 
                row, col = (i - 1) // n, (i - 1) % n
                next = board[~row][col if row % 2 == 0 else ~col]
                if next < 0:
                   next = i
                if next == n * n:
                    return rolls_count[curr] + 1
                if next not in rolls_count:
                    rolls_count[next] = rolls_count[curr] + 1
                    queue.append(next)
        return -1
    
def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]], 4)
    ]
    for case in cases:
        expected = case[1]
        judge(solution.snakesAndLadders(case[0]), expected)

    
   