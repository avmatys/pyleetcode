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


# https://leetcode.com/problems/minimum-window-substring/
class Solution:

    @timeit
    def minWindow(self, s: str, t: str) -> str:
        # Count nuber of occurs for each char
        char_freq = Counter(t)
        # Use 2 pointers to find a window
        left, right = 0, 0
        min_idx, min_size = 0, float('inf')
        counter = 0
        while right < len(s):
            # Check if we have this digit availalble in the freq map
            char_freq[s[right]] -= 1 # This will be negative if multiple not needed letters will be on the left side
            if char_freq[s[right]] >= 0:
                counter += 1
            right += 1
            # Now we should check if we found the desired len of the string
            while counter == len(t):
                # We should compare new window size with prev one
                if right - left < min_size:
                    min_idx = left
                    min_size = right - left
                # We should check if left one is present in the char freq
                char_freq[s[left]] += 1
                if char_freq[s[left]] > 0: # This check refers to line char_freq[s[right]] -= 1
                    counter -= 1
                left += 1
        return "" if min_size == float('inf') else s[min_idx : min_idx + min_size]


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (("bba", "ab"), "ba"),
        (("ADOBECODEBANC", "ABC"), "BANC"),
        (("a", "a"), "a"),
        (("a", "aa"), ""),        
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.minWindow(*input), expected)

    
   