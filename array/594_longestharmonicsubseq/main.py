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


# https://leetcode.com/problems/longest-harmonious-subsequence/
class Solution:

    @timeit
    def findLHS(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
           freq[num] = freq.get(num, 0) + 1
        max_length = 0
        for num in freq.keys():
            if num + 1 in freq:
                max_length = max(max_length, freq[num] + freq[num + 1])
        return max_length


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
                ([1,3,2,2,5,2,3,7], 5),
                ([1,2,3,4], 2),
                ([1,1,1,1], 0)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.findLHS(input), expected)

   
    