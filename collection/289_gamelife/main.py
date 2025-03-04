from typing import List
from datetime import datetime
import math

# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper

# https://leetcode.com/problems/game-of-life/description/
class Solution:

    @timeit
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        def is_live(row, col):
            neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1), 
                         (1, 1), (-1, -1), (-1, 1), (1, -1)]
            live_count = 0
            for i, j in neighbors:
                neigh_row = row + i
                if neigh_row < 0 or neigh_row >= rows:
                    continue 
                neigh_col = col + j
                if neigh_col < 0 or neigh_col >= cols:
                    continue 
                if board[neigh_row][neigh_col] % 2 == 1:
                    live_count += 1
                if live_count > 3:
                    break
            if board[row][col] % 2 == 1:
                if live_count == 2 or live_count == 3:
                    return True
            else:
                if live_count == 3:
                    return True
            return False

        for i in range(rows):
            for j in range(cols):
                if is_live(i, j):
                    board[i][j] += 2
        for i in range(rows):
            for j in range(cols):
                board[i][j] //= 2
    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    for i in range(len(result)):
        assert result[i] == expected[i]
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([[1,1],[1,0]], [[1,1],[1,1]]),
        ([[0,1,0],[0,0,1],[1,1,1],[0,0,0]], [[0,0,0],[1,0,1],[0,1,1],[0,1,0]])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        solution.gameOfLife(input)
        judge(input, expected)


    
   