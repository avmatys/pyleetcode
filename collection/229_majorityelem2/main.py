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


# https://leetcode.com/problems/majority-element-ii/
class Solution:

    @timeit
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        first_cnt = 0
        second_cnt = 0
        first, second = -1, -1
        for i in range(n):
            if first == nums[i]:
                first_cnt += 1
            elif second == nums[i]:
                second_cnt += 1
            elif first_cnt == 0:
                first = nums[i]
                first_cnt += 1
            elif second_cnt == 0:
                second = nums[i]
                second_cnt += 1
            else:
                first_cnt -= 1
                second_cnt -= 1

        first_cnt = 0
        second_cnt = 0
        for num in nums:
            if num == first:
                first_cnt += 1
            elif num == second:
                second_cnt += 1

        result = []
        if first_cnt > n//3:
            result.append(first)
        if second_cnt > n//3:
            result.append(second)
        return result        


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([1,2,3,1], [1]),
        ([1,2,1,1,2,2,2], [1,2]),
        ([1,2], [1,2]),
        ([2,1,1,3,1,4,5,6], [1])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.majorityElement(input), expected)

    
   