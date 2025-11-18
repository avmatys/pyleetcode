from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        dirs = [(0,1), (1,0), (1,1), (1,-1), (0,-1), (-1,0), (-1,-1), (-1,1)]
        m, n = len(board), len(board[0])
        stack = [click]
        while stack:
            i, j = stack.pop()
            if board[i][j] == 'M':
                board[i][j] = 'X'
                break
            elif board[i][j] == 'E':
                cnt = 0
                nxt = []
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if ni < 0 or ni >= m: continue
                    if nj < 0 or nj >= n: continue
                    if board[ni][nj] == 'M': cnt += 1
                    nxt.append([ni, nj])
                if cnt == 0:
                    board[i][j] = 'B'
                    stack += nxt
                else:
                    board[i][j] = str(cnt)
        return board

