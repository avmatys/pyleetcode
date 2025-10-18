from typing import List

class Solution:
    """
    seq:
                   A B A B A B
    x mod 3 = 1 -> 1 1 2 1 2 1...
    x mod 3 = 2 -> 2 2 1 2 1 2...
    """
    def stoneGameIX(self, stones: List[int]) -> bool:
        rmd = [0] * 3
        for x in stones:
            rmd[x % 3] += 1
        # No chance for Alice
        if rmd[1] == rmd[2] == 0:
            return False
        # To win needed one pair
        if rmd[0] % 2 == 0: 
            return min(rmd[1], rmd[2]) > 0
        # To win needed at least 2 nums diff
        return abs(rmd[1] - rmd[2]) > 2

