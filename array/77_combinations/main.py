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

# https://leetcode.com/problems/combinations
class Solution:

    @timeit
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def generate(start, combs):
            if len(combs) == k:
                result.append(combs[:])
                return
            for i in range(start + 1, n + 1):
                combs.append(i)
                generate(i, combs)
                combs.pop()
        generate(0, [])
        return result
        

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    for i in range(len(result)):    
        assert result[i] == expected[i]
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
      ((4,2), [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]),
      ((1,1), [[1]])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.combine(*input), expected)


    
   