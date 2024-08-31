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


# https://leetcode.com/problems/jump-game-ii/
class Solution:

    @timeit
    # Slow solution
    def jump(self, nums: List[int]) -> int:

        # Init array to save min number of ways to reach to the i-th element
        num_count = len(nums)
        dp = [1000000] * num_count
        dp[0] = 0
        
        for i in range(num_count):      
            # Iterate throuh all availalble steps
            for step in range(1, nums[i] + 1):
                dp_idx = i + step
                if dp_idx >= num_count:
                    break
                dp[dp_idx] = min(dp[dp_idx], dp[i] + 1)
           
        return dp[num_count-1]

    # Solution with good performance
    def jump2(self, nums: List[int]) -> int:
        
        max_idx = 0
        last_level_idx = 0
        jumps = 0
        
        for i in range(len(nums) - 1):
            # Find max idx, to which we can jump, consider max_idx as a level (layer)
            max_idx = max(max_idx, i + nums[i])
            print(f"i {i} nums[i] {nums[i]} Max {max_idx} Last layer {last_level_idx} Jumps {jumps}")
            # Check if we checked all points at current level
            if last_level_idx == i:
                # We should do additional jump to go to the next level
                jumps += 1
                # We should update our last level index
                last_level_idx = max_idx

        return jumps



def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
                ([2,3,1,1,4], 2),
                ([2,3,1,0,4], 2)
            ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.jump(input), expected)
        judge(solution.jump2(input), expected)

    
   