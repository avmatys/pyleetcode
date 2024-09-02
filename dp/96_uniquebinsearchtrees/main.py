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


# https://leetcode.com/problems/unique-binary-search-trees/description/
class Solution:

    @timeit
    def numTrees(self, n: int) -> int:

        # Base for dp
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1

        # Each tree contains left and righ subtrees
        # Number of the possible trees = num of left subtress * num of right subtrees
        # dp[i] stores number of subrees, build from i vertexes
        # We start calculation from the 2 vertexes and later reuse previous calculations
        for current_num in range(2, n + 1):
            for left in range(current_num):
                right = current_num - left - 1 # We should extract 1 because it's a head vertex
                dp[current_num] += dp[left] * dp[right] 

        return dp[n]


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (2, 2),
        (3, 5),
        (4, 14),
        (19, 1767263190)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.numTrees(input), expected)

    
   