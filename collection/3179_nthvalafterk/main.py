from typing import List

class Solution:

    # Simple prefix sum approach
    def valueAfterKSeconds2(self, n: int, k: int) -> int:
        prefix = [1] * n
        for _ in range(k):
            for i in range(1, n):
                prefix[i] += prefix[i-1]
        return prefix[-1] % (10**9 + 7)

    
    # Approach with Pascal's Triangle
    def valueAfterKSeconds3(self, n: int, k: int) -> int:
        N = k + n - 1
        r = n - 1
        return comb(N, r) % (10**9 + 7)


    # Pascal's triangle without build in funcion
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        N = k + n - 1
        r = n - 1
        res = 1
        for i in range(1, min(k, r) + 1):
            res = res * (N - i + 1) // i
        return res % (10 ** 9 + 7)
