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

# https://leetcode.com/problems/keyboard-row/description
class Solution:

    @timeit
    def findWords(self, words: List[str]) -> List[str]:
        rows = [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]

        # Iterate word one by one
        result = []
        for word in words:
            # Try to find correct row based on first char
            lower_word = word.lower()
            for row in rows:
                if lower_word[0] not in row:
                    continue
                # Iterate through chars in word
                i = 1
                n = len(lower_word)
                while i < n and lower_word[i] in row:
                    i += 1
                if i == n:
                    result.append(word)
        
        return result


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ((["Hello","Alaska","Dad","Peace"]), ["Alaska","Dad"]),
        ((["omk"]), []),
        ((["adsdf","sfd"]), ["adsdf","sfd"])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.findWords(input), expected)


    
   