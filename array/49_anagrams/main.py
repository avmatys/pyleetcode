from typing import List
from datetime import datetime
import heapq


# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper


# https://leetcode.com/problems/group-anagrams
class Solution:

    @timeit
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()
        for str in strs:
            sorted_str = ''.join(sorted(str))
            if sorted_str not in anagrams:
                anagrams[sorted_str] = []
            anagrams[sorted_str].append(str)
        result = list(anagrams.values())
        return result


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    for array in expected:
        assert array in expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ((["eat","tea","tan","ate","nat","bat"]), [["bat"],["nat","tan"],["ate","eat","tea"]]),
        (([""]), [[""]]),
        ((["a"]), [["a"]]),
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.groupAnagrams(input), expected)


    
   