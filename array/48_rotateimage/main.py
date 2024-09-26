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


# https://leetcode.com/problems/rotate-image/description/
class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for row in range(n//2):
            for col in range(row, n - row - 1):
                matrix[row][col], matrix[n-col-1][row] = matrix[n-col-1][row], matrix[row][col]
                matrix[n-col-1][row], matrix[n-row-1][n-col-1] = matrix[n-row-1][n-col-1],matrix[n-col-1][row]
                matrix[n-row-1][n-col-1], matrix[col][n-row-1] = matrix[col][n-row-1], matrix[n-row-1][n-col-1]


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([[1,2,3],[4,5,6],[7,8,9]], [[7,4,1],[8,5,2],[9,6,3]]),
        ([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]],[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]),
        ([[1]], [[1]]),
        ([[1,2],[3,4]], [[3,1],[4,2]])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        solution.rotate(input)
        judge(input, expected)

    
   