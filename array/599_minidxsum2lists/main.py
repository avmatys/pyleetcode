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
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        first_list_map = dict()
        for idx, place in enumerate(list1):
            first_list_map[place] = idx
        min_idx_sum = 9999
        output = []
        for idx, place in enumerate(list2):
            if place not in first_list_map:
                continue
            curr_idx_sum = first_list_map[place] + idx
            if curr_idx_sum < min_idx_sum:
                output.clear()
                output.append(place)
                min_idx_sum = curr_idx_sum
            elif curr_idx_sum == min_idx_sum:
                output.append(place)
        return output
    


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
                ((["Shogun","Tapioca Express","Burger King","KFC"], ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]), ["Shogun"]),
                ((["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Shogun","Burger King"]), ["Shogun"]),
                ((["happy","sad","good"],["sad","happy","good"]), ["sad","happy"])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.findRestaurant(*input), expected)

   
    