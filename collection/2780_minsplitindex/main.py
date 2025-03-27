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


# https://leetcode.com/problems/minimum-index-of-a-valid-split
class Solution:

    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        dom_i = -1
        for i in range(n):
            if cnt == 0 or i == 0:
                dom_i = i
            if nums[dom_i] == nums[i]:
                cnt += 1
            else:
                cnt -= 1
        total_cnt = 0
        for num in nums:
            if num == nums[dom_i]:
                total_cnt += 1
        curr_cnt = 0
        for i in range(n):
            if nums[i] == nums[dom_i]:
                curr_cnt += 1
            if curr_cnt > (i + 1) // 2 and total_cnt - curr_cnt > (n - i - 1) // 2:
                return i
        return -1


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([1,2,2,2], 2)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.minimumIndex(input), expected)

    
   
