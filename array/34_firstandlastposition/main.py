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


# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
       
        n = len(nums)
        
        left = 0
        right = n - 1

        start_position = -1
        end_position = -1

        while left <= right:
            mid = (left + right) // 2
            # We should look for a smaller num in left part of array
            if nums[mid] > target:
                right = mid - 1
            # We should look for a bigger num in right part of array
            elif nums[mid] < target:
                left = mid + 1
            # Value is equal to the targer
            else:
                # We should try to find the first and last position near the current index
                start_position =mid
                end_position = mid

                # Find a start
                start_left = left
                start_right = mid
                while start_left <= start_right:
                    start_mid = (start_left + start_right) // 2
                    # Our mid value is smaller than needed
                    if nums[start_mid] < target:
                        start_left = start_mid + 1
                    # Our value is correct one, but we should try to find a better case 
                    else:
                        start_position = start_mid
                        start_right = start_mid - 1

                # Find end
                end_left = mid
                end_right = right
                while end_left <= end_right:
                    end_mid = (end_left + end_right) // 2
                    # Our mid value is smaller than needed
                    if nums[end_mid] > target:
                        end_right = end_mid - 1
                    # Our value is correct one, but we should try to find a better case 
                    else:
                        end_position = end_mid
                        end_left = end_mid + 1
                
                # We are done
                break


        return [start_position, end_position]



def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([5,7,7,8,8,10], 8), [3,4]),
        (([5,7,7,8,8,10], 5), [0,0]),
        (([5,7,7,8,8,10], 10), [5,5]),
        (([1,1,1,1,1,1,1], 1), [0,6]),
        (([5,7,7,8,8,10], 6), [-1,-1]),
        (([1], 2), [-1,-1]),
        (([], 1), [-1,-1])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.searchRange(*input), expected)

    
   