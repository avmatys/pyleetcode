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


# https://leetcode.com/problems/integer-to-english-words/description/?envType=daily-question&envId=2024-08-06
class Solution:

    @timeit
    def numberToWords(self, num: int) -> str:

        num_less_ten = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        num_less_twenty = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        num_less_hundred = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        # Handle zero
        if num == 0:
            return "Zero"
     
        # Recursive function to get word
        def convert_to_words(num: int):
            if num < 10:
                return num_less_ten[num]
            if num < 20:
                return num_less_twenty[num-10]
            if num < 100:
                return num_less_hundred[num // 10] + ( " " + convert_to_words(num % 10) if num % 10 > 0 else "")
            if num < 1000:
                return num_less_ten[num // 100] + " Hundred" + ( " " + convert_to_words(num % 100) if num % 100 > 0 else "")
            if num < 1000000:
                return convert_to_words(num // 1000) + " Thousand" + ( " " + convert_to_words(num % 1000) if num % 1000 > 0 else "")
            if num < 1000000000:
                return convert_to_words(num // 1000000) + " Million" + ( " " + convert_to_words(num % 1000000) if num % 1000000 > 0 else "")
            else:
                return convert_to_words(num // 1000000000) + " Billion" + ( " " + convert_to_words(num % 1000000000) if num % 1000000000 > 0 else "")
            
        return convert_to_words(num)



def judge(result: str, expected: str):
    print(f'Result:   {result}')
    print(f'Expected: {expected}')
    assert result.capitalize() == expected.capitalize()
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (0, "Zero"),
        (5, "Five"),
        (10, "Ten"),
        (15, "Fifteen"),
        (21, "Twenty One"),
        (42, "Forty Two"),
        (99, "Ninety Nine"),
        (60, "Sixty"),
        (123, "One Hundred Twenty Three"),
        (400, "Four Hundred"),
        (12345, "Twelve Thousand Three Hundred Forty Five"),
        (1234567,"One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"),
        (0, "Zero"),
        (1000010, "One Million Ten")
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.numberToWords(input), expected)

    
   