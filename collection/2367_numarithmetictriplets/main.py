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


# https://leetcode.com/problems/number-of-arithmetic-triplets/description/
class Solution:

    def bin_search(self, nums, left, right, target):
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return -1

    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n = len(nums)
        result = 0
        for j in range(1, n - 1):
            if self.bin_search(nums, 0, j, nums[j] - diff) < 0:
                continue
            if self.bin_search(nums, j, n, nums[j] + diff) < 0:
                continue
            result += 1
        return result


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([0,1,4,6,7,10], 3), 2)    
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.arithmeticTriplets(*input), expected)

    
   
