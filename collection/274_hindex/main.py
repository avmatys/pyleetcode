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

# https://leetcode.com/problems/h-index/
class Solution:

    @timeit
    def hIndex(self, citations: List[int]) -> int:
        paper_count = len(citations)
        buckets = [0 for i in range(paper_count + 1)]
        for cit in citations:
            if cit >= paper_count:
                buckets[paper_count] += 1
            else:
                buckets[cit] += 1
        h = -1
        running_sum = 0
        for i in range(paper_count, -1, -1):
           running_sum += buckets[i]
           if running_sum >= i:
               h = i
               break
        return h

class SolutioRev:
    def hIndex(self, citations: List[int]) -> int:
        count = [0] * 1001
        for c in citations:
            count[c] += 1
        h, csum = 1001, 0
        while csum < h:
            h -= 1
            csum += count[h]
        return h

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([3,0,6,1,5], 3),
        ([0], 0),
        ([1,3,1], 1),
        ([1,1,1,1], 1)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.hIndex(input), expected)


    
   
