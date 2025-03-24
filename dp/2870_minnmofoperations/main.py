from typing import List
from datetime import datetime
from collections import Counter


def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper

# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/description/ 
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        total = 0
        for value in counter.values():
            if value == 1:
                return -1
            total += (value + 2) // 3
        return total
        
    
if __name__ == '__main__':
    solution = Solution()    
    assert 4 == solution.minOperations([2,2,3,3,2,4,4,4,4,4])
