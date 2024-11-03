from typing import List
from datetime import datetime


# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper


# https://leetcode.com/problems/word-search/description/
class Solution:

    @timeit
    def exist(self, board: List[List[str]], word: str) -> bool:

        # Specify vars
        rows = len(board)
        cols = len(board[0])
        str_len = len(word)
        visited = set()

        def find_word(row_idx: int, col_idx: int, word_idx: int):
            # Succesfull condition to finish
            if word_idx == str_len:
                return True
            # Filter not ok cases
            curr_cell = (row_idx, col_idx)
            if row_idx < 0 or row_idx >= rows or col_idx < 0 or col_idx >= cols or curr_cell in visited or board[row_idx][col_idx] != word[word_idx]:
                return False
            
            # Mark as visited
            visited.add(curr_cell)
            # Find all possible cases and continue
            result = find_word(row_idx + 1, col_idx, word_idx + 1) or find_word(row_idx, col_idx + 1, word_idx + 1) or \
                        find_word(row_idx - 1, col_idx, word_idx + 1) or find_word(row_idx, col_idx - 1, word_idx + 1)
            
            visited.remove(curr_cell)
            return result
        
        # Find all possilbe first symbols
        for i in range(rows):
            for j in range(cols):
                if find_word(i, j, 0):
                   return True

        return False


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result ==  expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"), True),
        (([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"), True),
        (([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "PP"), False)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.exist(*input), expected)


    
   