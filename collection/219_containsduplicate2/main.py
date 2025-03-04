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

# https://leetcode.com/problems/contains-duplicate-ii/description
class Solution:

    @timeit
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_idxs = {}
        for i, num in enumerate(nums):
            if num not in num_idxs:
                num_idxs[num] = i
            else:
                prev_idx = num_idxs[num]
                if i - prev_idx <= k:
                    return True
                else:
                    num_idxs[num] = i 
        return False
    
    
        

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([1, 2, 3, 1], 3), True),
        (([1, 2, 3, 1], 2), False),
        (([1, 0, 1, 1], 1), True),
        (([1, 2, 3, 1, 2, 3], 2), False)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.containsNearbyDuplicate(*input), expected)


    
   