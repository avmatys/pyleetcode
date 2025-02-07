from typing import List
from datetime import datetime
from typing import Optional
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

# https://leetcode.com/problems/max-points-on-a-line/description/
class Solution:

    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 3:
            return n
        max_count = 2
        for i in range(n):
            lines = dict()
            max_curr = 2
            x0 = points[i][0]
            y0 = points[i][1]
            for j in range(i + 1, n):
                x1 = points[j][0]
                y1 = points[j][1]
                A = y1 - y0
                B = x0 - x1
                C = A*x0 + B*y0
                d = math.gcd(A,B,C)
                d = d if d > 0 else 1
                a,b,c = A/d, B/d, C/d
                if c < 0:
                    c = -c
                if a < 0 and b < 0:
                    a = -a
                    b = -b
                elif a <= 0 or b <= 0:
                    a = -a if a > 0 else a 
                    b = -b if b < 0 else b 
                key = (a,b,c)
                if key in lines:
                    lines[key] += 1
                    max_curr = max(max_curr, lines[key])
                else:
                    lines[key] = 2
            max_count = max(max_count, max_curr)
        return max_count


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([[0,1],[0,0],[0,4],[0,-2],[0,-1],[0,3],[0,-4]], 7),
        ([[0,0],[-1,-1],[2,2]], 3),
        ([[0,0],[1,-1],[1,1]], 2),
        ([[0,0],[4,5],[7,8],[8,9],[5,6],[3,4],[1,1]], 5),
        ([[0,0],[1,-1],[1,1]], 2),
        ([[0,0],[-1,-1],[2,2]], 3),
        ([[1,1],[2,2],[3,3]], 3),
        ([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]], 4),
        ([[0,0],[0,1]], 2),
        ([[0,0]], 1),
        ([[1,0],[2,0],[0,0],[100,0]], 4),
        ([[1,1],[2,1],[3,1],[-100,1]], 4),
        ([[4,1],[4,-199],[4,-1000000],[4,0]], 4)     
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        result = solution.maxPoints(input)
        judge(result, expected)

    
   