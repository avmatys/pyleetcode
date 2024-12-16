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


# https://leetcode.com/problems/maximum-length-of-pair-chain/description/
class Solution:

    @timeit
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        curr = float('-inf')
        count = 0
        for pair in pairs:
            if pair[0] > curr:
                curr = pair[1]
                count += 1
        return count


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
                ([[1,2],[2,3],[3,4]], 2),
                ([[1,2],[7,8],[4,5]], 3)
            ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.findLongestChain(input), expected)

   
    