from typing import List
from datetime import datetime
from collections import deque

# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper

# https://leetcode.com/problems/sliding-window-median/description/
import heapq

class Solution:

   def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        n = len(nums)
        max_heap = []
        min_heap = []
        # Build 2 heaps
        # In the min heap - the smallest element is greater than median or the part of median (even length)
        # In the max heap - the biggest one is median
        for i in range(k):
            heapq.heappush(max_heap, (-nums[i], i))
        for _ in range(k//2):
            x, i = heapq.heappop(max_heap)
            heapq.heappush(min_heap, (-x, i))
        # Process data 1 by 1 and mantain total heap len equal to k
        res = [self.find_median(max_heap, min_heap, k)]
        for i in range(k, n):
            x = nums[i]
            # Current value is smaller that the biggest value in the max heap -> store in the max one
            if x <= -max_heap[0][0]:
                heapq.heappush(max_heap, (-x, i))
                # If you shrinked value is from min heap
                # -> we should balance our heaps
                # -> get biggest from max heap and add to the min heap
                # If our shrinked value is from the max heap
                # -> we will be in balance as we add 1 element just before
                if nums[i - k] >= -max_heap[0][0]:
                    x1, i1 = heapq.heappop(max_heap)
                    heapq.heappush(min_heap, (-x1, i1))
            else:
                heapq.heappush(min_heap, (x, i))
                # Explanation is the same as above for the max heap
                # If shrinked value is smaller than median value
                # This means that from max heap value will be removed and data will be unbalanced
                # To avoid this we should extract smallest value from the min heap and add to the max heap
                if nums[i - k] <= -max_heap[0][0]:
                    x1, i1 = heapq.heappop(min_heap)
                    heapq.heappush(max_heap, (-x1, i1))
            # Srink
            while max_heap and max_heap[0][1] <= i - k:
                heapq.heappop(max_heap)
            while min_heap and min_heap[0][1] <= i - k:
                heapq.heappop(min_heap)
            res.append(self.find_median(max_heap, min_heap, k))
        return res

   def find_median(self, max_heap, min_heap, k):
       return -max_heap[0][0] * 1.0 if k % 2 > 0 else (min_heap[0][0] - max_heap[0][0]) / 2.0
