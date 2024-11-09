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


# https://leetcode.com/problems/surrounded-regions/description/
class Solution:


    def find_subregion(self, cell: tuple, board: List[List[int]]):
        
        rows = len(board)
        cols = len(board[0])
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        subregion = set([cell])
        queue = deque()
        queue.append(cell)

        while queue:
            curr_cell = queue.popleft()
            for direction in DIRECTIONS:
                next_cell = (curr_cell[0] + direction[0], curr_cell[1] + direction[1])
                next_i, next_j = next_cell
                if 0 <= next_i < rows and 0 <= next_j < cols and next_cell not in subregion and board[next_i][next_j] == 'O':
                    subregion.add(next_cell)
                    queue.append(next_cell)
        
        return subregion


    def is_border(self, idx: int, border_idx: int):
        return idx == 0 or idx == border_idx


    @timeit
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        visited_region = set()
        
        for i in range(rows):
            for j  in range(cols):
                cell = (i, j)
                if board[i][j] == 'O' and cell not in visited_region:
                    subregion = self.find_subregion((i, j), board)
                    surrounded = all(not self.is_border(sub_cell[0], rows - 1) and not self.is_border(sub_cell[1], cols -1) for sub_cell in subregion)
                    if surrounded:
                        for sub_cell in subregion:
                            sub_i, sub_j = sub_cell
                            board[sub_i][sub_j] = 'X'
                    else:
                        visited_region.update(subregion) 


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]), [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]),
        (([["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]), [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]),
        (([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","X","X","X"]]), [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","X","X","X"]])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        solution.solve(input)
        judge(input, expected)


    
   