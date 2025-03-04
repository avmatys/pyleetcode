from typing import List
from datetime import datetime
from typing import Optional
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

# https://leetcode.com/problems/minimum-genetic-mutation/description/
class Solution:

    def is_one_char_diff(self, g1, g2):
        n = len(g1)
        diff_count = 0
        for i in range(n):
            if g1[i] != g2[i]:
                diff_count += 1
            if diff_count > 1:
                return False
        return True 

    @timeit
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue = deque([startGene])
        visited = {startGene:0}
        while queue:
            curr = queue.popleft()
            for next in bank:
                if not self.is_one_char_diff(curr, next):
                    continue
                if next == endGene:
                    return visited[curr] + 1
                if next not in visited:
                    visited[next] = visited[curr] + 1
                    queue.append(next)
        return -1
    
def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (("AACCGGTT", "AACCGGTA", ["AACCGGTA"]), 1),
        (("AACCGGTT", "AACCGGTA", []), -1),
        (("AACCGGTT", "AAACGGTA",["AACCGGTA","AACCGCTA","AAACGGTA"]), 2),
    ]
    for case in cases:
        expected = case[1]
        judge(solution.minMutation(*case[0]), expected)

    
   