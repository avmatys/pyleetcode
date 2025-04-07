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

# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/
class Solution:

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        nums.sort(reverse=True)
        target_sum = sum(nums) / k
        visited = [False] * n
        cache = dict()
        def make_subset(idx, k, current_sum):
            # We succefully build k subsets
            if k == 0:
                return True
            # Check if we have already checked the same combination of numbers
            typle_visited = tuple(visited)
            if typle_visited in cache:
                return cache[typle_visited]
            # We found one more set with sum k
            if current_sum == target_sum:
                cache[typle_visited] = make_subset(0, k-1, 0)
                return cache[typle_visited]
            # Iterate through the rest of the numbers
            for new_idx in range(idx, n):
                if not visited[new_idx] and current_sum + nums[new_idx] <= target_sum:
                    visited[new_idx] = True
                    if make_subset(new_idx + 1, k, current_sum + nums[new_idx]):
                        return True
                    visited[new_idx] = False
            # Mark visited as unsuccesful
            cache[tuple(visited)] = False
            return cache[tuple(visited)]
        # Run the execution
        return make_subset(0, k, 0)
    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([4,3,2,3,5,2,1], 4), True)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.canPartitionKSubsets(*input), expected)

    
   
