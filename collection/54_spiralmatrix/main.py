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


# https://leetcode.com/problems/spiral-matrix/description
class Solution:

    @timeit
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        sequence = []
       
        row_cnt = len(matrix)
        col_cnt = len(matrix[0])

        top_row = 0
        bottom_row = row_cnt - 1
        right_col = col_cnt - 1
        left_col = 0

        curr_dir_idx = 0
        while len(sequence) < row_cnt * col_cnt:
            
            # Process top
            if curr_dir_idx == 0:
                for j in range(left_col, right_col + 1):
                    sequence.append(matrix[top_row][j])
                top_row += 1
            # Process right
            if curr_dir_idx == 1:
                for i in range(top_row, bottom_row + 1):
                    sequence.append(matrix[i][right_col])
                right_col -= 1
            # Process bottom
            if curr_dir_idx == 2:
                for j in range(right_col, left_col - 1, -1):
                    sequence.append(matrix[bottom_row][j])
                bottom_row -= 1
            # Process left
            if curr_dir_idx == 3:
                for i in range(bottom_row, top_row - 1, -1):
                    sequence.append(matrix[i][left_col])
                left_col += 1

            # Rotate
            curr_dir_idx += 1
            if curr_dir_idx >= 4:
                curr_dir_idx = 0
        
        return sequence


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([[1,2,3],[4,5,6],[7,8,9]]), [1,2,3,6,9,8,7,4,5]),
        (([[1,2,3,4],[5,6,7,8],[9,10,11,12]]), [1,2,3,4,8,12,11,10,9,5,6,7])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.spiralOrder(input), expected)


    
   