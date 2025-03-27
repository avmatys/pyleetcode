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


# https://leetcode.com/problems/partition-array-into-disjoint-intervals/description/
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        running_min = [nums[-1]] * n
        for i in range(n-2, -1, -1):
            running_min[i] = min(running_min[i + 1], nums[i])
        curr_max = nums[0]
        for i in range(1, n):
            curr_max = max(curr_max, nums[i-1])
            if curr_max <= running_min[i]:
                return i
        return -1

class SolutionRev:
    def partitionDisjoint(self, nums: List[int]) -> int:
        curr_max = nums[0]
        possible_max = nums[0]
        result = 1
        for i in range(len(nums)):
            if nums[i] < curr_max:
                curr_max = possible_max
                result = i + 1
            else:
                possible_max = max(possible_max, nums[i])
        return result


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([5,0,3,8,6], 3)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.partitionDisjoint(input), expected)

    
   
