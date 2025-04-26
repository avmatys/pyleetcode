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

# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        res = 0
        tmp = 0
        for i in range(n):
            if i < k:
                res += int(blocks[i] == 'W')
                tmp = res
            else:
                tmp += int(blocks[i] == 'W') - int(blocks[i-k] == 'W')
                res = min(res, tmp)
        return res
