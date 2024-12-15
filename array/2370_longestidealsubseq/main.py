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


# https://leetcode.com/problems/minimum-index-sum-of-two-lists/
class Solution:

    @timeit
    def longestIdealString(self, s: str, k: int) -> int:
        subseq_len = {ord(char): 0  for char in s}
        for char in s:
            code = ord(char)
            range_values = [subseq_len.get(code - i, 0) for i in range(k + 1)]
            max_len = max(range_values) + 1
            for i in range(k + 1):
                if (code - i) in subseq_len:
                    subseq_len[code - i] = max_len
        return max(subseq_len.values())
        
    @timeit
    def longestIdealStringDP(self, s: str, k: int) -> int:
        dp = [0] * 128
        for char in s:
            i = ord(char)
            dp[i] = max(dp[i - k : i + k + 1]) + 1
        return max(dp)

    


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
                (("acfgbd", 2), 4),
                (("abcd", 3), 4),
                (("arsmxbhgzx", 23), 10),
                (("lkpkxcigcs", 6), 7),
                (("ogferqbdmhvojugoftaaderxgnqgcupmvppzalukcwdsrzonopcovpllpltrvzejhjgbspcvvtevimrpqyhyxsjfhorwmxafnitzirtrcfmuclobutxitjrffdblopztxovakrlwzxkpwauahzvcbzulhfdbmnchpdzeohaatvzpywhusknkhjsqatkttynmeytiqfsmilocvleiohpxylcqaznzzxmpbupnczwlsdvdnhrnwvmsgcmckwcvzcqvrujyfygxwfwhsciozlikiuqmurrvbceobfdjmdhiawaxbasnxmaxirptnrkoohiobkedlaojlmxdgvyjspfyhsnuqliwhfuzkvtqznzgzmjljbbyeippkrsojwveupnznunmzxvjvnzrhxxbfwwbgksbhjuuqkgmcjkeswucfkofowdmuzjnwhsfgovbipcbqyyilyxxeswzvebdcjpwvqmdkewhzzbsjovltuvoqhjlxqydltfumxgunosuvvajfrhmewxldnvgmusvtugdhzjinxmcakggzrgvmhhaoeyyyubrxffazgpdwgsshqtixnpdogivkadxoaplxqwgkctqcwywhlkmnjrnzwlhyjnlhadjtbnlgxbzgjxcehbysuvooojcqnoaivtpwybfvycnnvxzlybmujfncqijtlwutrjwrbgrbjjnfkvrkcxbtzronzhkfdexdexpxwrtwoynbjwnqxgodffcweskjhoteezatgsjcobrqorgmgsccitcvczjlhttnnivytdewqanlkyekvkgzqedxjxcikokubmoydtkiideninxycxummcntkudrnvbzhbzfeishtecsgwjecnpjbmbwcfogyvwizbiakjjamulmgzbrvehyblxagrljiwccprmfjgbzjtymzqvswaxrxrvigwztehkmfywewqkkvhoqbedqiiicwhyxvckreftkpuelkekpqufbqzzilubyqwnkzchavxwlrzblxdgfqvacqdszfjkgartpdbyexzoutoybcuwyoxioqrrntybdlvzdrzrttfjcfuqqdliqmcqoydxsoppidi", 0), 53)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.longestIdealStringDP(*input), expected)

   
    