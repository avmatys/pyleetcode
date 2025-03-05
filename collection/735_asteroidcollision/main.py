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


# https://leetcode.com/problems/asteroid-collision/description
class Solution:

    @timeit
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            if ast > 0:
                stack.append(ast)
            else:
                while stack and stack[-1] > 0 and stack[-1] < -ast:
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(ast)
                elif stack and stack[-1] == -ast:
                    stack.pop()
        return stack
         

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([-2,-1,1,2], [-2,-1,1,2]),
        ([5,10,-5], [5,10]),
        ([8,-8], []),
        ([10,2,-5], [10])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.asteroidCollision(input), expected)
