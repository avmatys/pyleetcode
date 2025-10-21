from typing import List

class DetectSquares:

    def __init__(self):
        self.p = defaultdict(int)
        self.x = defaultdict(set)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.p[(x, y)] += 1
        self.x[y].add(x)

    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0
        for px in self.x[y]:
            if px == x: continue
            d = abs(x - px)
            res += self.p[(px,y)] * self.p[(x,y+d)] * self.p[(px,y+d)]
            res += self.p[(px,y)] * self.p[(x,y-d)] * self.p[(px,y-d)]
        return res

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
