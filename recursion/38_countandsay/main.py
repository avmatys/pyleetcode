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


# https://leetcode.com/problems/count-and-say/
class Solution:
    
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            seq = self.countAndSay(n - 1)
            i, n, result = 0, len(seq), ""
            while i < n:
                count = 1
                while i + count < n and seq[i] == seq[i + count]:
                    count += 1
                result += str(count) + seq[i]
                i += count
            return result



def judge(result: str, expected: str):
    print(f'Result:   {result}')
    print(f'Expected: {expected}')
    assert result.capitalize() == expected.capitalize()
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
	(4, "1211")
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.countAndSay(input), expected)

    
   
