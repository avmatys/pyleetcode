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


# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/description/
class Solution:

    @timeit
    # Solved using greedy approach as groups can be divided by N symbols
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        result = [words[0]]
        for i in range(1, len(groups)):
            if groups[i] != groups[i-1]:
                result.append(words[i])
        return result
    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ((["e","a","b"], [0,0,1]), ["e","b"]),
        ((["a","b","c","d"], [1,0,1,1]), ["a","b","c"]),
      
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.getLongestSubsequence(input[0], input[1]), expected)

    
   