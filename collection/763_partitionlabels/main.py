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


# https://leetcode.com/problems/partition-labels/description/
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        last_indexes = [-1] * 26
        for i in range(n):
            last_indexes[ord(s[i]) - 97] = i
        result = []
        start, last = 0, 0
        for i in range(n):
            last = max(last, last_indexes[ord(s[i]) - 97])
            if last == i:
                result.append(last - start + 1)
                start = last + 1
        return result

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ("ababcbacadefegdehijhklij", [9,7,8])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.partitionLabels(input), expected)

    
   
