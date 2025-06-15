from typing import List

class TimeMap:

    def __init__(self):
        self.buckets = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.buckets[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.buckets[key]
        n = len(values)
        l = 0
        r = n
        while l < r:
            m = l + (r - l) // 2
            if timestamp >= values[m][0]:
                l = m + 1
            else:
                r = m
        return "" if l == 0 else values[l - 1][1]

