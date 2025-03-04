from typing import List
from datetime import datetime
from collections import Counter


# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper


# https://leetcode.com/problems/unique-number-of-occurrences/description
class Solution:

    @timeit
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        return len(set(count.values())) == len(count.values())


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([1,2,2,1,1,3], True)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.uniqueOccurrences(input), expected)

    
   