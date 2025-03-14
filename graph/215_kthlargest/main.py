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

class MinHeap:

    def __init__(self, ):
        self.elements = []
        self.size = 0
    
    def left_child(self, i):
        return (2 * i) + 1
    
    def right_child(self, i):
        return (2 * i) + 2
    
    def parent(self, i):
        return (i - 1) // 2
    
    def add(self, elem):
        self.elements.append(elem)
        self.size += 1
        self.sift_up(self.size - 1)

    def sift_up(self, i):
        while i > 0:
            parent = self.parent(i)
            if self.elements[i] < self.elements[parent]:
                self.elements[i], self.elements[parent] = self.elements[parent], self.elements[i]
                i = parent
            else:
                break

    def sift_down(self, i):
        while i  < self.size // 2:
            left = self.left_child(i)
            right = self.right_child(i)
            new_i = left
            if right < self.size and self.elements[right] < self.elements[new_i]:
                new_i = right
            if self.elements[i] <= self.elements[new_i]:
                break
            self.elements[i], self.elements[new_i] = self.elements[new_i], self.elements[i]
            i = new_i

    def pop(self):
        if self.size == 0:
            return None
        self.elements[0], self.elements[-1] = self.elements[-1], self.elements[0]
        elem = self.elements.pop()
        self.size -= 1
        self.sift_down(0)
        return elem
    
    def peek(self):
        return self.elements[0]


class MinHeapRev:

    def __init__(self):
        self.elements = []
        self.size = 0

    def insert(self, value):
        self.elements.append(value)
        self.size += 1
        self.sift_up(self.size - 1)

    def sift_up(self, i):
        while 0 < i < self.size:
            parent = (i - 1) // 2
            if self.elements[i] < self.elements[parent]:
                self.elements[i], self.elements[parent] =  self.elements[parent], self.elements[i]
                i = parent
            else:
                break

    def sift_down(self, i):
        while 2 * i + 1 < self.size:
            left, right = 2 * i + 1, 2 * i + 2
            cmp = left
            if right < self.size and self.elements[right] < self.elements[cmp]:
                cmp = right
            if self.elements[i] > self.elements[cmp]:
                self.elements[i], self.elements[cmp] = self.elements[cmp], self.elements[i]
                i = cmp
            else:
                break

    def pop(self):
        if self.size == 0:
            return None
        self.elements[0], self.elements[self.size - 1] =  self.elements[self.size - 1], self.elements[0]
        value = self.elements.pop()
        self.size -= 1
        self.sift_down(0)
        return value

    def peek(self):
        if self.size == 0:
            return None
        return self.elements[0]

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = MinHeap()
        for num in nums:
            heap.insert(num)
            if heap.size > k:
                heap.pop()
        return heap.peek()


# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
class Solution:
    @timeit
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = MinHeap()
        for num in nums:
            heap.add(num)
            if heap.size > k:
                heap.pop()
        return heap.peek()
       

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([3,2,1,5,6,4], 2), 5),
        (([3,2,3,1,2,4,5,5,6], 4), 4),
        (([3,2,1,5,6,4], 1), 6),
        (([3,2,1,5,6,4], 6), 1),
        (([7,6,5,4,3,2,1], 5), 3),
    ]
    for case in cases:
        result = solution.findKthLargest(case[0][0][:], case[0][1])
        judge(result, case[1])
