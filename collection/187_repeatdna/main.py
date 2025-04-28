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

# https://leetcode.com/problems/repeated-dna-sequences/submissions/1620417236/
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        KMAP = {'A': 0b00, 'C': 0b01, 'G': 0b10, 'T': 0b11}
        MASK = 0xFFFFF
        dnas = dict()
        res = set()
        seq = 0
        n = len(s)
        for i in range(n):
            seq <<= 2
            seq |= KMAP[s[i]]
            seq &= MASK # Remove leading ones in the 32 bit as we need only 20 bits
            if i >= 9:
                if seq not in dnas:
                    dnas[seq] = 1
                else:
                    dnas[seq] += 1
                if dnas[seq] > 1 and seq not in res:
                    res.add(s[i - 9 : i + 1])
        return list(res)

