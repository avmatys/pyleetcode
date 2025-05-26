from typing import List

class StockPrice:

    def __init__(self):
        self.minpq = []
        self.maxpq = []
        self.values = {}
        self.latest = -1

    def update(self, timestamp: int, price: int) -> None:
        if timestamp > self.latest:
            self.latest = timestamp
        self.values[timestamp] = price
        heapq.heappush(self.minpq, (price, timestamp))
        heapq.heappush(self.maxpq, (-price, timestamp))

    def current(self) -> int:
        return self.values.get(self.latest, None)

    def maximum(self) -> int:
        while self.maxpq and -self.maxpq[0][0] != self.values[self.maxpq[0][1]]:
            heapq.heappop(self.maxpq)
        if self.maxpq:
            return -self.maxpq[0][0]
        return None

    def minimum(self) -> int:
        while self.minpq and self.minpq[0][0] != self.values[self.minpq[0][1]]:
            heapq.heappop(self.minpq)
        if self.minpq:
            return self.minpq[0][0]
        return None


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
