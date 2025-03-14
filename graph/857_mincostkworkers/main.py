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

# https://leetcode.com/problems/minimum-cost-to-hire-k-workers
class Solution:

     def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        ratio = sorted([(w / q, q) for w,q in zip(wage, quality)])
        heap = []
        total, cost = 0, float('inf')
        for p, q in ratio:
            heappush(heap, -q)
            total += q
            if len(heap) > k:
                total += heappop(heap)
            if len(heap) == k:
                cost = min(cost, total * p)
        return cost

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([10,20,5], [70,50,30], 2), 105.0)
    ]
    for case in cases:
        result = solution.mincostToHireWorkers(*case[0])
        judge(result, case[1])
