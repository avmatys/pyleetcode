from typing import List

class NumberContainers:

    def __init__(self):
        self.heaps = {}
        self.values = {}
        
    def change(self, index: int, number: int) -> None:
        if number not in self.heaps:
            self.heaps[number] = []
        heapq.heappush(self.heaps[number], index)
        self.values[index] = number

    def find(self, number: int) -> int:
        while self.heaps.get(number, []) and self.values.get(self.heaps[number][0], -1) != number:
            heapq.heappop(self.heaps[number])
        if self.heaps.get(number, []):
            return self.heaps[number][0]
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
