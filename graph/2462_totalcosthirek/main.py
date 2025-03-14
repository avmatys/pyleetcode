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

# https://leetcode.com/problems/total-cost-to-hire-k-workers/
class Solution:

    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        left_heap, right_heap = [], []
        left, right = 0, n - 1
        total = 0
        for _ in range(k):
            while len(left_heap) < candidates and left < right + 1:
                heappush(left_heap, costs[left])
                left += 1
            while len(right_heap) < candidates and left < right + 1:
                heappush(right_heap, costs[right])
                right -= 1
            if len(left_heap) == 0 and len(right_heap) == 0:
                break
            popleft = len(left_heap) > 0
            if popleft and len(right_heap) and right_heap[0] < left_heap[0]:
                popleft= False
            total += heappop(left_heap) if popleft else heappop(right_heap)
        return total


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([17,12,10,2,7,2,11,20,8], 3, 4), 11)
    ]
    for case in cases:
        result = solution.totalCost(*case[0])
        judge(result, case[1])
