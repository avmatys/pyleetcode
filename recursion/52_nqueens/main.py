from typing import List
from datetime import datetime


# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper


# https://leetcode.com/problems/n-queens-ii/description/
class Solution:

    def totalNQueens(self, n: int) -> List[List[str]]:

        # Helper method to check if board is valid with a new added queen
        def is_board_valid(board, row, col):
            # Check row to the left
            i, j = row, 0
            while j < col:
                if board[i][j] == 'Q':
                    return False
                j += 1
            # Left top diag
            i, j = row, col
            while i >= 0 and j >=0:
                if board[i][j] == 'Q':
                    return False
                i, j = i - 1, j - 1
            # Left bottom diag
            i, j = row, col
            while i < n and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i, j = i + 1, j - 1
            return True

        # Main method to solve a task using a backtracking
        def solve(board, col, result):
            if col == n:
                result.append([''.join(row) for row in board])
                return
            for i in range(n):
                if is_board_valid(board, i, col):
                    board[i][col] = 'Q'
                    solve(board, col + 1, result)
                    board[i][col] = '.'
                
        # Call main function
        board = [['.'] * n for _ in range(n)]
        result = []
        solve(board, 0, result)
        return len(result)


def judge(result: str, expected: str):
    print(f'Result:   {result}')
    print(f'Expected: {expected}')
    assert result == expected    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (4, 2),
        (1, 1),
        (2, 0)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.totalNQueens(input), expected)

    
   