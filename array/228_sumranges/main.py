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

# https://leetcode.com/problems/summary-ranges/description
class Solution:


    @timeit
    def summaryRanges(self, nums: List[int]) -> List[str]:               
        
        def build_range(start, end):
            if start == end:
                return f"{start}"
            else:
                return f"{start}->{end}"

            
        n = len(nums)
        result = []
        for i, num in enumerate(nums):
            # Start
            if i == 0:
                start = num
                expected = start + 1
            # Middle
            else:
                if num == expected:
                    expected += 1
                else:
                    result.append(build_range(start, expected - 1))
                    start = num
                    expected = start + 1
            # End
            if i == n - 1:
                result.append(build_range(start, expected - 1))

        return result
    
    
        

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([0,1,2,4,5,7]), ["0->2","4->5","7"]),
        (([0,2,3,4,6,8,9]), ["0","2->4","6","8->9"])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.summaryRanges(input), expected)


    
   