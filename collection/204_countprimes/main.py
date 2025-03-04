from typing import List
from datetime import datetime
import math


# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper


# https://leetcode.com/problems/count-primes/description/
class Solution:

    @timeit
    def countPrimes(self, n: int) -> int:  
        
        if n < 3:
            return 0
        
        array = [True for i in range(n+1)]
        array[0] = array[1] = False
        prime = 2
        while prime * prime <= n:
            if array[prime]:
                for i in range(prime*prime, n + 1, prime):
                    array[i] = False
            prime += 1
        
        count = 0
        for i in range(n):
            if array[i]:
                count += 1
      
        return count
    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [(10, 4),
             (1, 0),
             (3, 1),
             (4, 2)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.countPrimes(input), expected)

    
   