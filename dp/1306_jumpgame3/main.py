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

# https://leetcode.com/problems/jump-game-iii/ 
class Solution:

    def jump(self, arr, idx):
        if idx >= len(arr) or idx < 0 or arr[idx] == -1:
            return False
        if arr[idx] == 0:
            return True
        tmp = arr[idx]
        arr[idx] = -1
        return self.jump(arr, idx + tmp) or self.jump(arr, idx - tmp)

    def canReach(self, arr: List[int], start: int) -> bool:
        return self.jump(arr, start)


def judge(result: str, expected: str):
    print(f'Result:   {result}')
    print(f'Expected: {expected}')
    assert result == expected    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([4,2,3,0,3,1,2], 0), True)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.canReach(*input), expected)
   
