from typing import List
from datetime import datetime
from collections import deque 

# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper


# https://leetcode.com/problems/word-break/description/
class Solution:

    @timeit
    def evalRPN(self, tokens: List[str]) -> int:
        
        OPERATORS = set(['+', '-', '*', '/'])

        queue = deque()
        for token in tokens:
            if token not in OPERATORS:
                queue.append(int(token))
            else:
                right = queue.pop()
                left = queue.pop()
                if token == '+':
                    result = left + right
                elif token == '-':
                    result = left - right
                elif token == '*':
                    result = left * right
                elif token == '/':
                    result = int(left / right)
                queue.append(result) 

        return queue.pop()




def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ((["2","1","+","3","*"]), 9),
        ((["4","13","5","/","+"]), 6),
        ((["10","6","9","3","+","-11","*","/","*","17","+","5","+"]), 22)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.evalRPN(input), expected)


    
   