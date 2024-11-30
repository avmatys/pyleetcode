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


# https://leetcode.com/problems/remove-k-digits/
class Solution:

    @timeit
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if k >= n: 
            return "0"
        stack = []
        count = 0
        for digit in num:
            while stack and stack[-1] > digit and count < k:
                stack.pop()
                count += 1
            stack.append(digit)
        while count < k:
            stack.pop()
            count += 1
        while len(stack) > 1 and stack[0] == "0":
            stack = stack[1:]
        return "".join(stack)

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
             (("112", 1), "11"),
             (("1432219", 3), "1219"),
             (("10200", 1), "200"),
             (("10", 2), "0"),
             (("1562219", 3), "1219")
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.removeKdigits(*input), expected)

    
   