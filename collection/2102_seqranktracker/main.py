from typing import List
from datetime import datetime

class MinNode:
    def __init__(self, score, name):
        self.score = score
        self.name = name

    def __lt__(self, other):
        return (self.score < other.score) or (self.score == other.score and self.name > other.name)

class MaxNode:
    def __init__(self, score, name):
        self.score = score
        self.name = name

    def __lt__(self, other):
        return (self.score > other.score) or (self.score == other.score and self.name < other.name)

class SORTracker:

    def __init__(self):
        self.left = [] # Store k + 1 best values
        self.right = [] # Store other values
        self.k = 0

    def add(self, name: str, score: int) -> None:
        heapq.heappush(self.left, MinNode(score, name))
        if len(self.left) > self.k + 1:
            node = heapq.heappop(self.left)
            heapq.heappush(self.right, MaxNode(node.score, node.name))

    def get(self) -> str:
        res = self.left[0].name
        if self.right:
            node = heapq.heappop(self.right)
            heapq.heappush(self.left, MinNode(node.score, node.name))
        self.k += 1
        return res
        


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()
