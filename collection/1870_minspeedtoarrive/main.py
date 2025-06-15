from typing import List

class Solution:

    def calc_hours(self, dist, speed):
        res = 0.0
        for i, d in enumerate(dist):
            res = math.ceil(res)
            res += d / speed
        return res

    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        res = -1
        l = 1
        r = 10**7 + 1
        while l < r:
            m = l + (r - l) // 2
            if hour >= self.calc_hours(dist, m):
                r = res = m
            else:
                l = m + 1
        return res
