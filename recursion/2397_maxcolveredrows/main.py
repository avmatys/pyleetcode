from typing import List

class Solution:

    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:

        m, n = len(matrix), len(matrix[0])
        rows = [0] * m
        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    rows[i] |= (1 << j)
        self.res = 0

        def score(selected):
            res = 0
            mask = 0
            for col in selected:
                mask |= (1 << col)
            for row in rows:
                if row == 0 or row & mask == row:
                    res += 1
            return res

        def solve(col, selected):
            if len(selected) == numSelect:
                self.res = max(self.res, score(selected))
                return
            if col == n:
                return
            # Add curr
            selected.append(col)
            solve(col + 1, selected)
            selected.pop()
            # Skip curr
            solve(col + 1, selected)

        solve(0, [])
        return self.res
