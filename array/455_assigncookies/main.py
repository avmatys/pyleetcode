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


# https://leetcode.com/problems/assign-cookies/description/
class Solution:

    @timeit
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
       
        def quicksort(array: List[int]):
            
            n = len(array)
            if n <= 1:
                return array
            
            less = []
            equal = []
            greater = []

            pivot = array[0]
            for num in array:
                if num < pivot:
                    less.append(num)
                elif num == pivot:
                    equal.append(num)
                elif num > pivot:
                    greater.append(num)
            
            return quicksort(less) + equal + quicksort(greater)


        greed_factor = quicksort(g)
        cookie_size = quicksort(s)

        greed_idx = 0
        cookie_idx = 0

        result = 0
        while greed_idx < len(greed_factor) and cookie_idx < len(cookie_size):
            greed = greed_factor[greed_idx]
            cookie = cookie_size[cookie_idx]
            if greed <= cookie:
                result += 1
                greed_idx += 1
                cookie_idx +=1
            elif greed > cookie:
                cookie_idx += 1

        return result


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([1,2,3],[1,1]),1),
        (([1,2],[1,2,3]), 2),
        (([4,3,2,7,7,2,3,1],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7]),8)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.findContentChildren(*input), expected)


    
   