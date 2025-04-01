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

# https://leetcode.com/problems/frog-jump/description/
class Solution:

    def jump(self, stones, idx, k, n, dp):
        if idx == n - 1:
            return True
        if dp[idx][k] != -1:
            return dp[idx][k]
        result = 0
        for i in range(idx + 1, n):
            if k - 1 <= stones[i] - stones[idx] <= k + 1:
                result = result or self.jump(stones, i, stones[i] - stones[idx], n, dp)
            if stones[i] - stones[idx] > k + 1:
                break
        dp[idx][k] = result
        return result

    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = [[-1 for _ in range(n + 1)] for _ in range(n - 1)]
        return bool(self.jump(stones, 0, 0, n, dp))


def judge(result: str, expected: str):
    print(f'Result:   {result}')
    print(f'Expected: {expected}')
    assert result == expected    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([0,1,3,5,6,8,12,17], True)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.canCross(input), expected)

    
   
