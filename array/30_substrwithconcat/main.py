from typing import List
from datetime import datetime
from collections import Counter, defaultdict


# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper


# https://leetcode.com/problems/substring-with-concatenation-of-all-words/d
class Solution:

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # Count word count in array
        words_count = Counter(words)
        # Word len is important as this will be the size of the step
        word_len = len(words[0])
        # We will iterate for an offset from 0 to word_len
        result = []
        for offset in range(word_len):
            # After this we will use sliding window
            window_words_count = 0
            seen_words = defaultdict(int)
            i = offset
            while i + word_len <= len(s):
                # We get current word
                subs = s[i:i + word_len]
                # If word is not in the map - this means that we should reset seen and continue
                if subs not in words_count:
                    window_words_count = 0
                    seen_words.clear()
                # Word is in the map
                else:
                    # Update number of word occurence for the current offset case
                    window_words_count += 1
                    seen_words[subs] += 1
                    # We should check if we didn't exeed number of the words (like in map we have foo:2, but right now we have foo:3)
                    while seen_words[subs] > words_count[subs]:
                        # This means that we should make the sliding window smaller from the left
                        left_word = s[i - word_len * (window_words_count - 1) : i - word_len * (window_words_count - 2)]
                        seen_words[left_word] -= 1
                        window_words_count -= 1
                    # We are here - this means that everything is ok and we can compare size of our sliding window with total number of words
                    if window_words_count == len(words):
                        result.append(i - (window_words_count - 1) * word_len)
                i += word_len
        return result



def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (("barfoothefoobarman", ["foo","bar"]), [0,9]),
        (("wordgoodgoodgoodbestword", ["word","good","best","word"]), []),
        (("barfoofoobarthefoobarman", ["bar","foo","the"]), [6,9,12]),
        (("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"]),[13])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.findSubstring(*input), expected)

    
   