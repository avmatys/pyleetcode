from typing import List, Optional
from datetime import datetime
import math

# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected

# https://leetcode.com/problems/put-marbles-in-bags/description/
class Solution:

    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        cuts = [0] * (n - 1)
        for i in range(n - 1):
            cuts[i] = weights[i] + weights[i+1]
        cuts.sort()
        result = 0
        for i in range(k - 1):
            result += cuts[n - i - 2] - cuts[i]
        return result


if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([1,3,5,1],2), 4)
    ]
    for case in cases:
        judge(solution.putMarbles(*case[0]), case[1])
    



    
   
