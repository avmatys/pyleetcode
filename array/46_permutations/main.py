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
                    current.append(num)
                    next_nums = nums[:]
                    next_nums.remove(num)
                    generate(current, next_nums)
                    current.pop()
    
        generate([], nums)
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
        judge(solution.permute(input), expected)

    
   