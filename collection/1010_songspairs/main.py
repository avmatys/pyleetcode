from typing import List

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        cnt = [0] * 60
        res = 0
        for t in time:
            cmd = t % 60
            res += cnt[(60 - cmd) % 60]
            cnt[cmd] += 1
        return res
