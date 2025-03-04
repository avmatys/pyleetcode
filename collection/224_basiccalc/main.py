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


# https://leetcode.com/problems/basic-calculator/
class Solution:

    @timeit
    def calculate(self, s: str) -> int:
        
        def execute_operation(sign, value):
            if sign == '-':
                stack.append(-value)
            elif sign == '+':
                stack.append(value)
            elif stack == '*':
                stack.append(stack.pop() * value)
            elif stack == '/':
                stack.append(int(stack.pop() / value))

        number, sign, stack = 0, "+", []
        idx = 0
        while idx < len(s):
            ch = s[idx]
            if ch.isdigit():
                number = 10 * number + int(ch)
            if ch in '-+/*':  
                
                execute_operation(sign, number)
                number, sign = 0, ch
            elif ch == '(':
                number, offset = self.calculate(s[idx + 1 : ])
                idx += offset
            elif ch == ')':
                execute_operation(sign, number)
                return sum(stack), idx + 1 # This will be like an offset                   
            idx += 1
        execute_operation(sign, number)
        return sum(stack)


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ("1 + 1", 2),
        (" 2-1 + 2 ", 3),
        ("(1+(4+5+2)-3)+(6+8)", 23)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.calculate(input), expected)

    
   