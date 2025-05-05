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

# https://leetcode.com/problems/sliding-subarray-beauty/description/?envType=problem-list-v2&envId=sliding-window
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        window = [0] * 51 # Store here freq of negative nums
        res = []
        for i in range(len(nums)):
            if nums[i] < 0:
                window[-nums[i]] += 1
            if i >= k:
                if nums[i - k] < 0:
                    window[-nums[i-k]] -= 1
            if i >= k - 1:
                cnt = 0
                for j in range(50, -1, -1):
                    cnt += window[j]
                    if cnt >= x:
                        res.append(-j)
                        break
                if cnt < x:
                    res.append(0)
        return res

