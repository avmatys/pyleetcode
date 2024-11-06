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


# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii
class Solution:

    @timeit
    def removeDuplicates(self, nums: List[int]) -> int:

        n = len(nums)
        if (n < 3):
            return n
        
        k = 2
        for i in range(2, n):
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1
            
        return k


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    k, nums = expected
    assert result[0] == k
    for i in range(k):
        assert result[1][i] == nums[i]
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([0,0,0,1,1,1,2,2,2,3,3,3]), (8, [0,0,1,1,2,2,3,3,"_","_","_"])),
        (([1,1,1,2,2,3]), (5, [1,1,2,2,3,"_"])),
        (([0,0,1,1,1,1,2,3,3]), (7, [0,0,1,1,2,3,3,"_","_"])),
        (([1,2,2]), (3, [1,2,2]))
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge((solution.removeDuplicates(input), input), expected)


    
   