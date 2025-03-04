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


# https://leetcode.com/problems/set-matrix-zeroes/description
class Solution:

    @timeit
    def setZeroes(self, matrix: List[List[int]]) -> None:
       
        row_count = len(matrix)
        column_count = len(matrix[0])

        first_row = False
        first_column = False

        # Check if there is a zero in first row, set frow to True.
        for i in range(column_count):
            if matrix[0][i] == 0:
                first_row = True

        # Check if there is a zero in first column, set fcol to True.
        for i in range(row_count):
            if matrix[i][0] == 0:
                first_column = True

        # Iterate through columns and set zero to the first row or column if zero is in the column
        for i in range(row_count):
            for j in range(column_count):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
 
        # Set needed columns and rows equal to zero except first row and column
        for i in range(1, row_count):
            if matrix[i][0] == 0:
                for j in range(1, column_count):
                    matrix[i][j] = 0
        for j in range(1, column_count):
            if matrix[0][j] == 0:
                for i in range(1, row_count):
                    matrix[i][j] = 0

        # Hande first row and column
        if first_column:
            for i in range(row_count):
                matrix[i][0] = 0
        if first_row:
            for j in range(column_count):
                matrix[0][j] = 0
        return matrix


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([[1,1,1],[1,0,1],[1,1,1]]), [[1,0,1],[0,0,0],[1,0,1]]),
        (([[0,1,2,0],[3,4,5,2],[1,3,1,5]]), [[0,0,0,0],[0,4,5,0],[0,3,1,0]])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.setZeroes(input), expected)


    
   