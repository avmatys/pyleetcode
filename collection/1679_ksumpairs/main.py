from typing import List
from datetime import datetime
from collections import Counter


# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper


# https://leetcode.com/problems/max-number-of-k-sum-pairs/description
class Solution:

    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = Counter(num for num in nums if num < k)
        result = 0
        for val in counter:
            result += min(counter[val], counter[k - val])
        return result // 2
    
class SolutionRev:
    def maxOperations(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums) - 1
        sorted_nums = sorted(nums)
        count = 0
        while left < right:
            curr_sum = sorted_nums[left] + sorted_nums[right]
            if curr_sum == k:
                count += 1
                right -= 1
                left += 1
            elif curr_sum > k:
                right -= 1
            else:
                left += 1
        return count

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected


if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([1,2,3,4,5], 5), 2)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.maxOperations(*input), expected)

    
   