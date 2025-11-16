from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        m, n = len(image), len(image[0])
        refc = image[sr][sc]

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or image[i][j] == color:
                return
            if image[i][j] != refc:
                return
            image[i][j] = color
            for di, dj in [(0,1), (0,-1)]:
                dfs(i + di, j + dj)
                dfs(i + dj, j + di)

        dfs(sr, sc)
        return image
