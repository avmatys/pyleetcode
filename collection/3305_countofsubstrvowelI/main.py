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

# https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-i/
class Solution:

    def count(self, word, k):
        vowel = {'a', 'e', 'i', 'o', 'u'}
        freq = dict()
        ucnt = 0
        ccnt = 0
        res = 0
        l = 0
        for r in range(len(word)):
            if word[r] in vowel:
                freq[word[r]] = freq.get(word[r], 0) + 1
                if freq.get(word[r], 0) == 1:
                    ucnt += 1
            else:
                ccnt += 1
            while ccnt >= k and ucnt == 5:
                if word[l] in vowel:
                    if freq.get(word[l], 0) == 1:
                        ucnt -= 1
                    freq[word[l]] -= 1
                else:
                    ccnt -= 1
                l += 1
            res += l
        return res
            

    def countOfSubstrings(self, word: str, k: int) -> int:
        return self.count(word, k) - self.count(word, k + 1)

        
