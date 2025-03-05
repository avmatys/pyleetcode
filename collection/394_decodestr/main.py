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

# https://leetcode.com/problems/decode-string/description/
class Solution:

    @timeit
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                res = ''
                while stack and stack[-1] != '[':
                    res = stack.pop() + res
                stack.pop() # remove bracket
                repeat = ''
                while stack and stack[-1].isdigit() :
                    repeat = stack.pop() + repeat
                stack.append(res * int(repeat))
        return ''.join(stack)

class SolutionRecursive:

    @timeit
    def decodeString(self, s: str) -> str:
        def helper(idx):
            result = ''
            number = 0
            while idx < len(s):
                if s[idx] == '[':
                    substr, idx = helper(idx + 1)
                    result = result + (substr * number)
                    number = 0
                elif s[idx] == ']':
                    return result, idx
                elif s[idx].isdigit():
                    number = 10 * number + int(s[idx])
                else:
                    result += s[idx]
                idx += 1
            return result, idx
        return helper(0)[0]


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected

if __name__ == '__main__':
    solution = Solution()
    solution_rec = SolutionRecursive()
    cases = [
        ('2[jk]e1[f]', 'jkjkef'),
        ('pq1[2[jk]e1[f]]', 'pqjkjkef'),
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.decodeString(input), expected)
        judge(solution_rec.decodeString(input), expected)
