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


# https://leetcode.com/problems/determine-if-two-strings-are-close/
class Solution:

    @timeit
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        cnt1, cnt2 = Counter(word1), Counter(word2)
        if cnt1.keys() != cnt2.keys():
            return False
        if sorted(cnt1.values()) != sorted(cnt2.values()):
            return False
        return True
        
    def closeStrings2(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return
        freq1, freq2 = [0] * 26, [0] * 26
        for ch in word1:
            freq1[ord(ch)-ord('a')] += 1
        for ch in word2:
            freq2[ord(ch)-ord('a')] += 1
        for i in range(26):
            if freq1[i] == 0 and freq2[i] != 0: 
                return False
            if freq2[i] == 0 and freq1[i] != 0: 
                return False
        if freq1.sort() != freq2.sort():
            return False
        return True

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (('abc', 'bca'), True)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.closeStrings2(*input), expected)

    
   