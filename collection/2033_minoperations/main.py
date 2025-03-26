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


# https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/description/
class Solution:

    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Make flat list
        n,m = len(grid), len(grid[0])
        nums = []
        for i in range(n):
            for j in range(m):
                nums.append(grid[i][j])
        # Check if we can make a uni value grid
        if x > 1:
            remainder = nums[0] % x
            for num in nums[1:]:
                if num % x != remainder:
                    return -1
        # Find median of the array
        nums.sort()
        median = nums[len(nums) // 2]
        # Count number of operations
        total = 0
        for num in nums:
            total += abs(num-median) // x
        return total


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([[2,4],[6,8]], 2), 4)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.minOperations(*input), expected)

    
   
