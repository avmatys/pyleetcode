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


# https://leetcode.com/problems/valid-sudoku/
class Solution:

    @timeit
    def isValidSudoku(self, board: List[List[str]]) -> bool:  

        board_size = 9
        square_size = 3

        # Validate line and column
        square_status = [[-1 for _ in range(square_size)] for _ in range(square_size)]
        for idx in range(9):
            row_idx = idx 
            col_idx = idx
            # Check row
            nums = set()
            for j in range(board_size):
                if board[row_idx][j] == '.':
                    continue
                if board[row_idx][j] in nums:
                    return False
                nums.add(board[row_idx][j])
            # Check column
            nums = set()
            for i in range(board_size):
                if board[i][col_idx] == '.':
                    continue
                if board[i][col_idx] in nums:
                    return False
                nums.add(board[i][col_idx])
            # Check square
            sq_row_idx = row_idx // square_size
            sq_col_idx = col_idx % square_size
            if square_status[sq_row_idx][sq_col_idx] == -1:
                # Square was not checked before
                nums = set()
                board_row_idx = square_size * sq_row_idx
                board_col_idx = square_size * sq_col_idx
                for sq_i in range(board_row_idx, board_row_idx + square_size):
                    for sq_j in range(board_col_idx, board_col_idx + square_size):
                        if board[sq_i][sq_j] == '.':
                            continue
                        if board[sq_i][sq_j] in nums:
                            return False
                        nums.add(board[sq_i][sq_j])
                square_status[sq_row_idx][sq_col_idx] = 1
        return True
                         

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]), True),
        (([["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]), False)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.isValidSudoku(input), expected)


    
   