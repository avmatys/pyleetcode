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


# https://leetcode.com/problems/reshape-the-matrix/
class Solution:

    @timeit
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        in_rows, in_cols = len(mat), len(mat[0])
        if r * c != in_rows * in_cols:
            return mat
        result = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r * c):
            result[i // c][i % c] = mat[i // in_cols][i % in_cols]
        return result


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([[1,2],[3,4]], 1, 4), [[1,2,3,4]]),
        (([[1,2],[3,4]], 2, 4), [[1,2],[3,4]]),
        (([[1,2],[3,4]], 4, 1), [[1],[2],[3],[4]])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.matrixReshape(*input), expected)

    
   