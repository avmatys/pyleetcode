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

# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/description/
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        count = Counter(nums)
        for num in nums:
            start = num
            while count[start - 1] > 0:
                start -= 1
            while start <= num:
                while count[start] > 0:
                    for nextc in range(start, start + k):
                        if count[nextc] == 0:
                            return False
                        count[nextc] -= 1
                start += 1
        return True

