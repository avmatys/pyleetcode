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

# https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/description/
class Solution:

    # Solution by @votrubac
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort(key=lambda x: x[0])
        l, r = 0, 0
        wndw = 0
        res = 0
        n = len(tiles)
        while r < n and res < carpetLen:
            # Enough len to cover
            if (tiles[l][0] + carpetLen > tiles[r][1]):
                wndw += tiles[r][1] - tiles[r][0] + 1
                res = max(res, wndw)
                r += 1
            # Can cover only some part
            else:
                part = max(0, tiles[l][0] + carpetLen - tiles[r][0])
                res = max(res, wndw + part)
                wndw -= (tiles[l][1] - tiles[l][0] + 1)
                l += 1
        return res
