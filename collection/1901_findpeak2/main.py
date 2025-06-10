from typing import List

class Solution:

    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        l = 0
        r = m - 1
        while l < r:
            m = l + (r - l) // 2
            if max(mat[m+1]) >= max(mat[m]):
                l = m + 1
            else:
                r = m
        return (l, mat[l].index(max(mat[l])))
