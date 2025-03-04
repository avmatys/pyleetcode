from typing import List
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


# https://leetcode.com/problems/subsets-ii/description/
class Solution:

    @timeit
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range (1, n + 1)]
        result = []
        k -= 1
        while n > 0:  
            n -= 1
            idx, k = divmod(k, math.factorial(n))
            result.append(str(nums[idx]))
            nums.pop(idx)
        return ''.join(result)
            
     

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ((3, 2), "132"),
        ((4, 9), "2314"),
        ((3, 3), "213"),
        ((3, 1), "123")
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.getPermutation(*input), expected)

   
    