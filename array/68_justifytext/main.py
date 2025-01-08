from typing import List
from datetime import datetime
import math

# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper

# https://leetcode.com/problems/text-justification/
class Solution:

    @timeit
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        line_idx = 0
        idx = 0
        n = len(words)
        while idx < n:
            if line_idx + 1 > len(lines):
                lines.append({"left" : False, "words_cnt": 0, "words_len": 0, "words":[]})
            word = words[idx]
            word_len = len(word)
            if lines[line_idx]["words_len"] + lines[line_idx]["words_cnt"] + word_len <= maxWidth:
                lines[line_idx]["words_len"] += word_len
                lines[line_idx]["words_cnt"] += 1
                lines[line_idx]["words"].append(word)
                if idx == n - 1 and n > 0:
                    lines[line_idx]["left"] = True
                idx += 1
            else:
                if lines[line_idx]["words_cnt"] == 1:
                    lines[line_idx]["left"] = True
                line_idx += 1

        print(lines)
        result = []
        for line in lines:
            if line["left"]:
                spaces = " " * (maxWidth - line["words_len"] - line["words_cnt"] + 1)
                result.append(" ".join(line["words"]) + spaces)
            else:
                slots_cnt = line["words_cnt"] - 1
                min_space_cnt = (maxWidth - line["words_len"]) // slots_cnt
                spaces = [min_space_cnt] * slots_cnt
                remain_spaces = maxWidth - (min_space_cnt * slots_cnt) - line["words_len"]
                idx = 0
                while remain_spaces > 0:
                    spaces[idx] += 1
                    idx += 1
                    remain_spaces -= 1
                result_line = []
                for i in range(line["words_cnt"]):
                    result_line.append(line["words"][i])
                    if i < slots_cnt:
                        result_line.append(" " * spaces[i])
                result.append("".join(result_line))

        return result


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ((["This", "is", "an", "example", "of", "text", "justification."], 16),["This    is    an","example  of text","justification.  "]),
        ((["What","must","be","acknowledgment","shall","be"], 16), ["What   must   be","acknowledgment  ","shall be        "]),
        ((["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20), ["Science  is  what we","understand      well","enough to explain to","a  computer.  Art is","everything  else  we","do                  "])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.fullJustify(*input), expected)


    
   