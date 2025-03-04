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


# https://leetcode.com/problems/spiral-matrix-iii/description/?envType=daily-question&envId=2024-08-08
class Solution:

    @timeit
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:

        def is_in_grid(curr_row: int, curr_col: int):
            return 0 <= curr_col < cols and 0 <= curr_row < rows
        
        # Store to vars
        curr_row = rStart
        curr_col = cStart

        # Prepare array for indexes
        spiral_steps = [[rStart, cStart]]        

        cycle_idx = 0
        while len(spiral_steps) < rows * cols:
            # Move to the right
            for _ in range(2*cycle_idx+1):
                curr_col += 1
                if is_in_grid(curr_row, curr_col):
                    spiral_steps.append([curr_row, curr_col])
            # Move down
            for _ in range(2*cycle_idx+1):
                curr_row += 1
                if is_in_grid(curr_row, curr_col):
                    spiral_steps.append([curr_row, curr_col])
            # Move left
            for _ in range(2*(cycle_idx+1)):
                curr_col -= 1
                if is_in_grid(curr_row, curr_col):
                    spiral_steps.append([curr_row, curr_col])
            # Move up
            for _ in range(2*(cycle_idx+1)):
                curr_row -= 1
                if is_in_grid(curr_row, curr_col):
                    spiral_steps.append([curr_row, curr_col]) 
            # Go to the next cycle
            cycle_idx += 1
        return spiral_steps
    

    def spiralMatrixIIIRotate(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
       
        # Store to vars
        curr_row = rStart
        curr_col = cStart

        # Prepare array for indexes
        spiral_steps = []   

        # Set direction for move
        direction_row = 0
        direction_col = 1
       
        # Count number of moves
        steps = 1 # Each number of steps should be executed twice 
        next_steps = 2 # Each next step is greater on 1 than prev one
        sides_count = 0

        while len(spiral_steps) < rows * cols:

            # Store to the list if conditions are met
            if 0 <= curr_col < cols and 0 <= curr_row < rows:
                spiral_steps.append([curr_row, curr_col])
            
            # Update row and col index
            curr_row += direction_row
            curr_col += direction_col
            steps -= 1

            # We executed all steps for one side
            if steps == 0:
                # Change direction clockwis
                direction_row, direction_col = direction_col, -direction_row
                # Update number of processed sides
                sides_count += 1 
                # We should go to another pair of sides, number of steps is greater on one
                if sides_count == 2:
                    sides_count = 0
                    steps = next_steps
                    next_steps += 1
                # We have one step - the same number of steps
                else:
                    steps = next_steps - 1
        
        return spiral_steps
                    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ((1, 4, 0 ,0), [[0,0],[0,1],[0,2],[0,3]]),
        ((5, 6, 1, 4), [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]),
        ((3, 3, 2, 2), [[2,2],[2,1],[1,1],[1,2],[2,0],[1,0],[0,0],[0,1],[0,2]])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.spiralMatrixIII(input[0], input[1], input[2], input[3]), expected)
        judge(solution.spiralMatrixIIIRotate(input[0], input[1], input[2], input[3]), expected)

    
   