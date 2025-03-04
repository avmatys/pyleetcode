from typing import List
from datetime import datetime
import heapq

# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper

# https://leetcode.com/problems/keyboard-row/description
class Solution:

    @timeit
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        # Returns index in the array or -1 if not found
        def search(target: int, values: List[int]):
            start = 0
            end = len(values)
            while start < end:
                middle = (start + end) // 2
                if values[middle] == target:
                    return middle
                elif values[middle] < target:
                    start = middle + 1
                else:
                    end = middle
            return -1

        # Get elements in a sorted order
        heap = score[:]
        heapq.heapify(heap)
        n = len(heap)
        sorted_scores = [heapq.heappop(heap) for _ in range(n)]

        # Iterate through initial array
        result = [-1 for _ in range(n)]
        for i, elem in enumerate(score):
            rank = search(elem, sorted_scores)
            if rank == n - 1:
                result[i] = "Gold Medal"
            elif rank == n - 2:
                result[i] = "Silver Medal"
            elif rank == n - 3:
                result[i] = "Bronze Medal"
            else:
                result[i] = str(n - rank) 

        return result


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([5,4,3,2,1]), ["Gold Medal","Silver Medal","Bronze Medal","4","5"]),
        (([10,3,8,9,4]), ["Gold Medal","5","Bronze Medal","Silver Medal","4"])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.findRelativeRanks(input), expected)


    
   