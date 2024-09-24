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


# https://leetcode.com/problems/permutations/
class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []
        def generate(current: List[int], nums: List[int]):
            if len(nums) == 0:
                result.append(current[:])
                return
            else:
                for num in nums:
                    next_current = current[:]
                    next_current.append(num)
                    next_nums = nums[:]
                    next_nums.remove(num)
                    generate(next_current, next_nums)
                    #current.pop()
    
        generate([], nums)
        return result


    def permute2(self, nums: List[int]) -> List[List[int]]:

        # Store new task here
        queue = deque()
        queue.append((nums, []))

        # Store path here
        result = []
        while queue:
            curr_nums, curr_path = queue.popleft()
            if len(curr_nums) == 0:
                result.append(curr_path)
            else:
                for i in range(len(curr_nums)):
                    next_nums = curr_nums[:i] + curr_nums[i+1:]
                    next_path = curr_path + [curr_nums[i]]
                    queue.append((next_nums, next_path))
        
        return result
  


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([1,2,3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]),
        ([0,1],[[0,1],[1,0]]),
        ([1], [[1]])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.permute2(input), expected)

    
   