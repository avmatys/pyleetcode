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


# https://leetcode.com/problems/can-place-flowers/description
class Solution:

    @timeit
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        size = len(flowerbed)
        i = 0
        while i < size:
            if n == 0:
                break
            if flowerbed[i] == 0:
                empty_left = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right = (i == size - 1) or (flowerbed[i + 1] == 0)
                if empty_left and empty_right:
                    flowerbed[i] = 1
                    n -= 1
                    i += 2
                else:
                    i += 1
            else:
                i += 2
        return n == 0


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
                (([1,0,0,0,0,1], 2), False),
                (([1,0,0,0,1], 1), True),
                (([1,0,0,0,1], 2), False),
                (([0,0,1,0,0], 1), True),
                (([0], 1), True),
                (([0], 2), False)
               
            ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.canPlaceFlowers(*input), expected)

   
    