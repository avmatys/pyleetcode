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

# https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/description/
class Solution:

    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        # Prepare initial data to avoid duplicates
        unique_mat = [sorted(set(row)) for row in mat]
        m = len(unique_mat)
        # Prepare variable to store min diff and storage to avoid not needed computation
        min_diff = float('inf')
        memo = [set() for _ in range(m + 1)]
        def calc_sum(idx, curr_sum):
            nonlocal min_diff
            if idx == m:
                min_diff = min(min_diff, abs(target - curr_sum))
                return
            if curr_sum not in memo[idx]:
                memo[idx].add(curr_sum)
                for num in unique_mat[idx]:
                    calc_sum(idx + 1, curr_sum + num)
                    if min_diff == 0 or curr_sum + num > target:
                        break
        calc_sum(0, 0)
        return min_diff


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([[1,2,3],[4,5,6],[7,8,9]], 13), 0)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.minimizeTheDifference(*input), expected)

    
   
