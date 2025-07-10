from typing import List

class Solution:

    def can_build(self, power, min_power, stations, r):
        n = len(power)
        extra = [0] * (n + 1)
        for j in range(n):
            if j > 0:
                extra[j] += extra[j-1]
            curr = power[j] + extra[j]
            if curr >= min_power:
                continue
            needed = min_power - curr
            if needed > stations:
                return False
            stations -= needed
            extra[j] += needed
            extra[min(n, j+2*r+1)] -= needed
        return True

    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        # Calculate powers for each stations
        n = len(stations)
        power = [0] * n
        power[0] = sum(stations[0:r+1])
        for i in range(1,n):
            power[i] = power[i-1]
            if i - r > 0:
                power[i] -= stations[i-r-1]
            if i + r < n:
                power[i] += stations[i+r]
        # Do bin search
        left = min(power) 
        right = max(power) + k
        while left < right:
            mid = (right + left) // 2
            if self.can_build(power[:], mid + 1, k, r):
                left = mid + 1
            else:
                right = mid
        return left

        
