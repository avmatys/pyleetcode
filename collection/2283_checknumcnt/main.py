from typing import List

class Solution:
    def digitCount(self, num: str) -> bool:
         n = len(num)
        freq = [0] * 10
        for i in range(n):
            freq[int(num[i])] += 1
        return all(freq[i] == int(num[i]) for i in range(n))
