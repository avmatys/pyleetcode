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


# https://leetcode.com/problems/kth-distinct-string-in-an-array/description/?envType=daily-question&envId=2024-08-05
class Solution:

    @timeit
    def kthDistinct(self, arr: List[str], k: int) -> str:
        str_count = {}
        # Find frequency of each str
        for elem_str in arr:
            if elem_str in str_count:
                str_count[elem_str] += 1
            else:
                str_count[elem_str] = 1
        
        kth_str = ""
        # Iterate in the correct order (initial array) and return K th str
        for elem_str in arr:
            if str_count[elem_str] == 1:
                k -= 1
            if k == 0:
                kth_str = elem_str
                break
        return kth_str

    @timeit
    def kthDistinctTwoSets(self, arr: List[str], k: int) -> str:

        unique_set = set()
        unique_set.add(arr[0])
        non_unique_set = set()

        # Find unique and non unique elements
        for i in range(1, len(arr)):
            if arr[i] in unique_set:
                unique_set.remove(arr[i])
                non_unique_set.add(arr[i])
            elif arr[i] not in non_unique_set:
                unique_set.add(arr[i])

        # Simple validation to avoid loop
        if len(unique_set) < k:
            return ""
        
        # Find kth element in the original array
        kth_str = ""
        for i in range(len(arr)):
            if arr[i] in unique_set:
                k -= 1
            if k == 0:
                kth_str = arr[i]
                break
        return kth_str




    
if __name__ == '__main__':
    solution = Solution()
    assert "a" == solution.kthDistinctTwoSets(["d","b","c","b","c","a"], 2)
    assert "aaa" == solution.kthDistinctTwoSets(["aaa","aa","a"], 1)
    assert "" == solution.kthDistinctTwoSets(["a","b","a"], 3)
   