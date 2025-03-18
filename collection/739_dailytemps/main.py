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


# https://leetcode.com/problems/daily-temperatures/
class Solution:

    @timeit
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
      
        n = len(temperatures)
        result = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            temp = temperatures[i]
            while stack and temperatures[stack[-1]] <= temp:
               stack.pop()
            result[i] = stack[-1] - i if stack else 0
            stack.append(i)
        return result

class SolutionRev:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if stack:
                result[i] = stack[-1] - i
            stack.append(i)
        return result        


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
             ([73,74,75,71,69,72,76,73], [1,1,4,2,1,1,0,0]),
             ([30,40,50,60], [1,1,1,0])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.dailyTemperatures(input), expected)

    
   
