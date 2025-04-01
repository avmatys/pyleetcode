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

# https://leetcode.com/problems/minimum-sideway-jumps/description/
class Solution:

    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        dp = [1, 0, 1] # Store the lates line
        for i in range(n):
            if obstacles[i] > 0:
                dp[obstacles[i] - 1] = float('inf')
            for j in range(3):
                if obstacles[i] - 1 != j:
                    dp[j] = min(dp[j], min(dp[(j + 1) % 3], dp[(j + 2) % 3]) + 1)
        return min(dp)


def judge(result: str, expected: str):
    print(f'Result:   {result}')
    print(f'Expected: {expected}')
    assert result == expected    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([0,1,2,3,0], 2)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.minSideJumps(input), expected)

    
   
