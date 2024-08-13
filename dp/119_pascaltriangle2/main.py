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


# https://leetcode.com/problems/pascals-triangle-ii/description/
class Solution:

    @timeit
    def getRow(self, rowIndex: int) -> List[int]:
        
        # Init pascal triangle with initial value
        row = [1]
        
        # Calc triangle
        for idx in range(1, rowIndex+1):
            new_row = [1] * (idx + 1)
            print(f"{idx} {new_row} {row}")
            for elem_idx in range(1, idx):
                new_row[elem_idx] = row[elem_idx-1] + row[elem_idx]
            print(f"{idx} {new_row} {row}")
            row = new_row

        return row

    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (3, [1, 3, 3, 1]),
        (4, [1, 4, 6, 4, 1]),
        (0, [1]),
        (1, [1, 1])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.getRow(input), expected)

    
   