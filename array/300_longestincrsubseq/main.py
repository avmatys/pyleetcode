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


# https://leetcode.com/problems/minimum-index-sum-of-two-lists/
class Solution:

    @timeit
    def lengthOfLIS(self, nums: List[int]) -> int:

        def bin_search(values, n):
            left = 0
            right = len(values) - 1
            while left < right:
                mid = (left + right) // 2
                if values[mid] == n:
                    return mid
                elif values[mid] < n:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        lis_tail = []
        for num in nums:
            if not lis_tail or lis_tail[-1] < num:
                lis_tail.append(num)
            else:
                idx = bin_search(lis_tail, num)
                lis_tail[idx] = num
        return len(lis_tail)
    


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
                ([10,9,2,5,3,7,101,18], 4),
                ([0,1,0,3,2,3], 4),
                ([7,7,7,7,7,7,7], 1),
                ([0,1,0,3,2,3,6,3,5,1], 5),
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.lengthOfLIS(input), expected)

   
    