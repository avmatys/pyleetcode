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

# https://leetcode.com/problems/integer-to-roman/description/
class Solution:

    @timeit
    def intToRoman(self, num: int) -> str:
        digit_count = int(math.log10(num)) + 1
        roman_vals = { 1 : "I", 4: "IV", 5: "V", 9: "IX", 
                      10 : "X", 40: "XL", 50 : "L", 90: "XC", 
                      100 : "C", 400: "CD", 500 : "D", 900: "CM", 
                      1000 : "M" }
        result = []
        while digit_count > 0:
            curr_power = 10 ** (digit_count - 1)
            curr_digit = num // curr_power
            if curr_digit == 0:
                digit_count -= 1
                continue
            curr_num = curr_digit * curr_power
            if curr_num in roman_vals:
                result.append(roman_vals[curr_num])
                num -= curr_num
                continue
            if curr_digit > 5:
                result.append(roman_vals[5 * curr_power])
                num -= 5 * curr_power
            else:
                result.append(roman_vals[curr_power])
                num -= curr_power
        return ''.join(result)
    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (3749, "MMMDCCXLIX"),
        (58, "LVIII"),
        (1994, "MCMXCIV"),
        (1999, "MCMXCIX")
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.intToRoman(input), expected)


    
   