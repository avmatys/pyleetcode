from typing import List
from datetime import datetime
from collections import deque

# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper


# https://leetcode.com/problems/count-sorted-vowel-strings/description/
class Solution:

    @timeit
    def generateParenthesis(self, n: int) -> List[str]:

        if n <= 0:
            return []
        
        result = []

        def generate(open_count: int, close_count: int, sequence: str):

            # Generation finished
            if open_count == close_count == n:
                result.append(sequence)
                return 
            
            # Generate open bracket
            if open_count < n:
                generate(open_count + 1, close_count, sequence + "(")

            # Generate close bracket
            if close_count < open_count:
                generate(open_count, close_count + 1, sequence + ")")
        
        generate(0, 0, "")
        
        return result
    
    @timeit
    def generateParenthesisIterative(self, n: int) -> List[str]:
        
        if n <= 0:
            return []
        
        result = []
        queue = deque()
        queue.append((0, 0, ""))

        while len(queue) > 0:
            
            # Get entry
            open, close, sequence = queue.popleft()
            
            # Append finished str to the result array
            if open == close == n:
                result.append(sequence)
            
            # Continue processing - prepare new tasks
            if open < n:
                queue.append((open + 1, close, sequence + "("))

            # We can try to close brackets
            if close < open:
                queue.append((open, close + 1, sequence + ")"))

        return result
    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
                (1, ["()"]),
                (3, ["((()))","(()())","(())()","()(())","()()()"])  
            ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.generateParenthesisIterative(input), expected)