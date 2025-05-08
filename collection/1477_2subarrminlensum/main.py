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

# https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/description/
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        prefix = [float('inf')] * n
        suffix = [float('inf')] * n
        wsum = 0
        wlen = float('inf')
        l = 0
        for r in range(n):
            if wsum == target:
                wlen = min(wlen, r - l)
            prefix[r] = wlen
            wsum += arr[r]
            while wsum > target:
                wsum -= arr[l]
                l += 1
        res = float('inf')
        wsum = 0
        wlen = float('inf')
        r = n - 1
        for l in range(n - 1, -1, -1):
            wsum += arr[l]
            while wsum > target:
                wsum -= arr[r]
                r -= 1
            if wsum == target:
                wlen = min(wlen, r - l + 1)
            res = min(res, wlen + prefix[l])
        return -1 if res == float('inf') else res


