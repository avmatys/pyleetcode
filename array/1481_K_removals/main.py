from typing import List


# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/description/
class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        nums_count_map = {}
        for i in range(0, len(arr)):
            if arr[i] in nums_count_map:
                nums_count_map[arr[i]] += 1
            else:
                nums_count_map[arr[i]] = 1 
    
        count_map = {}
        for count in nums_count_map.values():
            if count in count_map:
                count_map[count] += 1
            else:
               count_map[count] = 1 

        key_set = set(count_map.keys())
        while k > 0:
            min_key = min(key_set)
            elem_count = min_key * count_map[min_key]
            if (k >= elem_count):
                key_set = key_set - {min_key}
                k -= elem_count
                count_map[min_key] = 0
            else:
                count_map[min_key] -= k//min_key
                break

        unique_count = sum(count_map.values())
        return unique_count
    

    def findLeastNumOfUniqueIntsNoMap(self, arr: List[int], k: int) -> int:
        
        length = len(arr)
        if length == 1:
            return 0 if k > 0 else 1
        if k == length:
            return 0
            
        arr.sort()
        count_list = [0] * (length+1)
        count = 1
        for i in range(1, length):
            if arr[i] == arr[i-1]:
                count += 1
            else:
                count_list[count] += 1
                count = 1
        count_list[count] += 1

        for i in range(1, length+1):
            if count_list[i] == 0:
                continue
            elem_count = i * count_list[i]
            if k >= elem_count:
                k -= elem_count
                count_list[i] = 0
            else:
                count_list[i] -= k//i
                break
        
        return sum(count_list)



    
if __name__ == '__main__':
    solution = Solution()
    assert 1 == solution.findLeastNumOfUniqueIntsNoMap([5,5,4], 1)
    assert 2 == solution.findLeastNumOfUniqueIntsNoMap([4,3,1,1,3,3,2], 3)
    assert 6 == solution.findLeastNumOfUniqueIntsNoMap([13,22,100,22,5,62,13,24,81,15,99,14,20,2,61,10,40,47,33,7,38,47,92,31,15,40,73,48,24,55,81,63,37,23,59,78,5,50,10,51,67,9,18,78,89,40,71,7,32,67,6,34,69,59,19,39,96,64,81,96,64,5,82,59,29,93,42,72,38,60,82,40,97,91,4,22,85,80,33,51,10,21,54,91,2,94,38,38,19,75,37,7,76,7,27,8,76,11,25,5], 78)
   

   