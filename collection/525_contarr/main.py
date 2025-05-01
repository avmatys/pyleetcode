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

# https://leetcode.com/problems/contiguous-array/description/
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """
        arr: 0,1,1,1,1,1,0,0,0
        f0:  1,1,1,1,1,1,2,3,4
        f1:  0,1,2,3,4,5,5,5,5
        1-0:-1,0,1,2,3,4,3,2,1
        """
        res = 0
        frq = dict()
        frq[0] = -1
        cnt = [0] * 2
        for i, num in enumerate(nums):
            cnt[num] += 1
            dff = cnt[1] - cnt[0]
            if dff in frq:
                res = max(res, i - frq[dff])
            else:
                frq[dff] = i
        return res

