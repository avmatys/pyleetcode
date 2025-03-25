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
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Use BFS solution
        words = set(wordDict)
        queue = deque([0])
        visited = set()

        str_length = len(s)
        while queue:
            current_idx = queue.popleft()
            if current_idx == str_length:
                return True

            for end_idx in range (current_idx + 1, str_length + 1):
                if end_idx in visited:
                    continue

                if s[current_idx:end_idx] in words:
                    queue.append(end_idx)
                    visited.add(end_idx)
                
        return False


class SolutionRev:
    def check(self, s, word_dict, memo):
        if s in memo:
            return memo[s]
        for i in range(len(s)):
            prefix = s[:i + 1]
            if prefix not in word_dict:
                continue
            suffix = s[i + 1 :]
            if len(suffix) == 0 or self.check(suffix, word_dict, memo):
                memo[s] = True
                return True
        memo[s] = False
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = dict()
        return self.check(s, set(wordDict), memo)

        
        


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (("leetcode", ["leet","code"]), True),
        (("leeeeetcode", ["leet","code"]), False),
        (("applepenapple",["apple","pen"]), True),
        (("catsandog", ["cats","dog","sand","and","cat"]), False)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.wordBreak(*input), expected)


    
   
