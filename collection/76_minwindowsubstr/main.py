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

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        substr_cnt, substr_total = [0] * 256, 0
        for ch in t:
            substr_cnt[ord(ch)] += 1
            substr_total += 1
        window_cnt, window_total = [0] * 256, 0
        left, min_idx, min_len = 0, -1, float('inf')
        for right in range(len(s)):
            rc = ord(s[right])
            # We should track this letter as it's in the substr
            if substr_cnt[rc] > 0:
                window_cnt[rc] += 1 # Add number of the such letters
                if window_cnt[rc] <= substr_cnt[rc]: # Check if we didn't exceed number of the needed letters in the substr
                    window_total += 1 
            # Check if we can make a window smaller
            while window_total >= substr_total:
                # Recalc min values
                curr_len = right - left + 1
                if curr_len < min_len:
                    min_idx, min_len = left, curr_len
                lc = ord(s[left])
                # We should track this letter as it's in the substring
                if substr_cnt[lc] > 0:
                    window_cnt[lc] -= 1 # Substract letter from the list
                    if window_cnt[lc] < substr_cnt[lc]: # Check if we still have enough letters to cover everything in the substr
                        window_total -= 1
                left += 1
        return "" if min_idx == -1 else s[min_idx:min_idx + min_len]      


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

    
   
