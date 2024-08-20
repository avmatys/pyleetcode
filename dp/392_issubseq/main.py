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


# https://leetcode.com/problems/is-subsequence/description/
class Solution:

    @timeit
    def isSubsequence(self, s: str, t: str) -> bool:
        # Return None if elem greated than target_value was not found
        def bin_search(values, target_value):
            left = 0
            right = len(values) - 1
            answer = None
            while left <= right:
                mid = (right + left) // 2
                if target_value >= values[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
                    answer = values[mid]      
            return answer

        # Simple check
        if len(t) < len(s):
            return False
        
        # Prepare a set with list of indexes of digits in t str
        dp = dict()
        for idx, ch in enumerate(t):
            ch_code = ord(ch) - 97 # a will have 0 code
            if ch_code in dp:
               dp[ch_code].append(idx)
            else:
               dp[ch_code] = [idx]

        # Check if s is substr of t
        last_ch_idx = -1
        for ch in s:
            # Char doesn't exist in the t string
            ch_code = ord(ch) - 97
            if ch_code not in dp:
                return False
            # Find next idx and check if it exists
            ch_idx_list = dp[ch_code]
            next_ch_idx = bin_search(ch_idx_list, last_ch_idx)
            if next_ch_idx == None:
                return False
            # Update last idx
            last_ch_idx = next_ch_idx
        
        return True           
    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (("abc", "ahbgdc"), True),
        (("axc", "ahbgdc"), False),
        (("ab", "baab"), True),
        (("rjufvjafbxnbgriwgokdgqdqewn", "mjmqqjrmzkvhxlyruonekhhofpzzslupzojfuoztvzmmqvmlhgqxehojfowtrinbatjujaxekbcydldglkbxsqbbnrkhfdnpfbuaktupfftiljwpgglkjqunvithzlzpgikixqeuimmtbiskemplcvljqgvlzvnqxgedxqnznddkiujwhdefziydtquoudzxstpjjitmiimbjfgfjikkjycwgnpdxpeppsturjwkgnifinccvqzwlbmgpdaodzptyrjjkbqmgdrftfbwgimsmjpknuqtijrsnwvtytqqvookinzmkkkrkgwafohflvuedssukjgipgmypakhlckvizmqvycvbxhlljzejcaijqnfgobuhuiahtmxfzoplmmjfxtggwwxliplntkfuxjcnzcqsaagahbbneugiocexcfpszzomumfqpaiydssmihdoewahoswhlnpctjmkyufsvjlrflfiktndubnymenlmpyrhjxfdcq"), False),
        (("leeeeetcode", "yyyyylyyyyyyyyyeyyyyyeyyyyyyeyyyyyyyeyyyyyyeyyyyyyyeyyyyeyyyyyyytyyyyyycyyyyyyoyyyyyyydyyyyyyyeyyyyy"), True),
        (("aaaaaa", "bbaaaa"), False)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.isSubsequence(input[0], input[1]), expected)

    
   