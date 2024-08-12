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


# https://leetcode.com/problems/pascals-triangle/description/
class Solution:

    @timeit
    def generate(self, numRows: int) -> List[List[int]]:
        
        # Init pascal triangle with initial value
        pascal_triangle = [[1 for _ in range(numRow+1)] for numRow in range(numRows)]
        
        for numRow in range(2, numRows):
            for elem_idx in range(1, numRow):
                pascal_triangle[numRow][elem_idx] = pascal_triangle[numRow-1][elem_idx-1] + pascal_triangle[numRow-1][elem_idx]

        return pascal_triangle

    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (5, [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]),
        (1, [[1]])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.generate(input), expected)

    
   