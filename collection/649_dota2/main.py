from typing import List
from datetime import datetime
from collections import deque

# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper

# https://leetcode.com/problems/dota2-senate/description/
class Solution:

    @timeit
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        queue = deque(senate)
        senator = ''
        senator_count = 0
        while queue and senator_count < len(senate):
            current_senator = queue.popleft()
            if senator == '':
                # means that senator is not initialized
                senator = current_senator
                senator_count = 1
                queue.append(senator)
            elif current_senator == senator:
                # this means that we met the same senator as before
                senator_count += 1 
                queue.append(senator)
            else:
                # we met another senator
                senator_count -= 1
                if senator_count == 0: 
                    senator = ''
        return 'Radiant' if queue[0]  == 'R' else 'Dire'


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ("RD", "Radiant"),
        ("RDD", "Dire"),
        ("DDRDDRRDRD", "Dire")
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.predictPartyVictory(input), expected)

   
    
