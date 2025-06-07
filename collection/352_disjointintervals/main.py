from typing import List

class DSU:

    def __init__(self):
        self.parents = dict()
        self.intervals = dict()

    def exists(self, x):
        return x in self.parents

    def make_set(self, x):
        self.parents[x] = x
        self.intervals[x] = [x, x]

    def find_set(self, x):
        if x not in self.parents:
            return None
        if self.parents[x] != x:
            self.parents[x] = self.find_set(self.parents[x])
        return self.parents[x]

    def union_set(self, x, y):
        # Get sets
        sx = self.find_set(x)
        sy = self.find_set(y)
        if sx is None or sy is None:
            return
        # Join x to y
        self.parents[sx] = sy
        x_interval = self.intervals[sx]
        del self.intervals[sx]
        self.intervals[sy] = [min(self.intervals[sy][0], x_interval[0]), max(self.intervals[sy][1], x_interval[1])]


class SummaryRanges:

    def __init__(self):
        self.dsu = DSU()

    def addNum(self, value: int) -> None:
        if self.dsu.exists(value):
            return
        self.dsu.make_set(value)
        self.dsu.union_set(value, value - 1)
        self.dsu.union_set(value, value + 1)

    def getIntervals(self) -> List[List[int]]:
        return sorted(self.dsu.intervals.values())



# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
