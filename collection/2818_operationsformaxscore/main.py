from typing import List
from datetime import datetime
import math

# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper


# https://leetcode.com/problems/apply-operations-to-maximize-score/description
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:

        n = len(nums)
        MOD = 1000000007

        # Calculate prime scores
        scores = [0] * n
        for i in range(n):
            num = nums[i]
            for factor in range(2, int(math.sqrt(num)) + 1):
                if num % factor == 0:
                    scores[i] += 1
                    while num % factor == 0:
                        num //= factor
            if num >= 2:
                scores[i] += 1
     
        # Calculate prev greater idx
        left = [-1] * n
        right = [n] * n
        stack = []
        for i in range(n):
            while stack and scores[stack[-1]] < scores[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        
        # Calculate next greater idx
        stack.clear()
        for i in range(n - 1, -1, -1):
            while stack and scores[stack[-1]] <= scores[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)
    
        # Sort indices based on nums[i]
        sorted_i = sorted(range(n), key=lambda i: -nums[i])

        # Calculate score
        score = 1
        for i in sorted_i:
            num = nums[i]
            operations = min((i - left[i]) * (right[i] - i), k)
            score = (score * pow(num, operations, MOD)) % MOD
            k -= operations
            if k == 0:
                break
        return score

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([19,12,14,6,10,18], 3), 4788)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.maximumScore(*input), expected)

    
   
