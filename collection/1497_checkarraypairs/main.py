from typing import List

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        buf = [0] * k
        for x in arr:
            rmdr = x % k
            pair = (k - rmdr) % k
            if buf[pair] > 0:
                buf[pair] -= 1
            else:
                buf[rmdr] += 1
        return sum(buf) == 0
