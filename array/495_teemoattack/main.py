from typing import List
from datetime import datetime
import sys

# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper


# https://leetcode.com/problems/teemo-attacking/description/
class Solution:

    @timeit
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
       
        n = len(timeSeries)
        result = 0
        for i in range(n):
            # Calc finish time
            time = timeSeries[i] + duration - 1 
            next = i + 1
            # Check if the finish time and text iteration are not intersected
            if next < n:
                time = min(time, timeSeries[next] - 1)
            result += time - timeSeries[i] + 1            
        return result



def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([1,4], 2), 4),
        (([1,2], 2), 3)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.findPoisonedDuration(*input), expected)


    
   