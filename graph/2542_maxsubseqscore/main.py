from typing import List
from datetime import datetime
from typing import Optional
import math
from heapq import heappush, heappop

# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper

# https://leetcode.com/problems/maximum-subsequence-score
class Solution:

    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        heap = []
        total, result = 0, 0
        for num1, num2 in sorted(list(zip(nums1, nums2)), key=lambda nums: -nums[1]):
            heappush(heap, num1)
            total += num1
            if len(heap) > k:
                total -= heappop(heap)
            if len(heap) == k:
                result = max(result, num2 * total)
        return result

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([1,3,3,2], [2,1,3,4], 3), 12)
    ]
    for case in cases:
        result = solution.maxScore(*case[0])
        judge(result, case[1])
