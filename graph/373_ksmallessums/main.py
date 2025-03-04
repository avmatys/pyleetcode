from typing import List
from datetime import datetime
from typing import Optional
import heapq

# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper

# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/
class Solution:
    @timeit
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n, m = len(nums1), len(nums2)
        def push(i, j):
           if i < n and j < m:
               heapq.heappush(queue, (nums1[i] + nums2[j], i, j))
        def pop():
            return heapq.heappop(queue)
        queue = []
        push(0, 0)
        result = []
        while queue and len(result) < k:
            _, i, j = pop() 
            result.append([nums1[i], nums2[j]])
            push(i, j + 1)
            if j == 0:
                push(i + 1, 0)
        return result 

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([1,7,11], [2,4,6], 3), [[1,2],[1,4],[1,6]]),
    ]
    for case in cases:
        result = solution.kSmallestPairs(*case[0])
        judge(result, case[1])