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


# https://leetcode.com/problems/search-a-2d-matrix/description/
class Solution:

    @timeit
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows * cols - 1
        while left <= right:
            mid = (left + right) // 2
            row_idx = mid // cols
            col_idx = mid % cols
            if matrix[row_idx][col_idx] == target:
                return True
            elif matrix[row_idx][col_idx] > target:
                right = mid - 1
            else:
                left = mid + 1     
        return False
    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3), True),
        (([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13), False)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.searchMatrix(*input), expected)


    
   