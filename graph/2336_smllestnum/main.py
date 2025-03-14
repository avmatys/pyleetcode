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

# https://leetcode.com/problems/smallest-number-in-infinite-set/description/
class SmallestInfiniteSet:

    def __init__(self):
        self.curr = 1
        self.heap = []
        self.added = set()

    def popSmallest(self) -> int:
        if self.heap:
            value = heappop(self.heap)
            self.added.remove(value)
        else:
            value = self.curr
            self.curr += 1
        return value        

    def addBack(self, num: int) -> None:
        if num < self.curr and num not in self.added:
            heappush(self.heap, num)
            self.added.add(num)


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected

if __name__ == '__main__':
    obj = SmallestInfiniteSet()
    param_1= obj.popSmallest()
    obj.addBack(num)
