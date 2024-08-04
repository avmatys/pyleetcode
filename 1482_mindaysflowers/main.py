from typing import List
from datetime import datetime


def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper


# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/
class Solution:

    @timeit
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        # Don't have enough flowers
        needed_count = m * k
        if needed_count > len(bloomDay):
            return -1
         
        low = min(bloomDay)
        high = max(bloomDay)

        while low < high:
            mid = (high + low) // 2
            bouqets_count = self.find_m_bouqets(mid, bloomDay, k, m)
            # Let's try to find a smaller day
            if bouqets_count >= m:
                high = mid
            # We didn't find a smaller day -> increase day
            else:
                low = mid + 1
        
        return low


    # Find m bouqets from k flowers from the grown
    def find_m_bouqets(self, day, grown_flowers: List[int], k: int, m: int) -> int:
        bouqets_count = 0
        flowers = 0
        for grown_day in grown_flowers:
            # Flowers should be adjacent 
            if grown_day <= day:
                flowers += 1
                if flowers == k:
                    bouqets_count += 1
                    flowers = 0
                    if bouqets_count == m:
                        break
            else:
                flowers = 0
        return bouqets_count



    
if __name__ == '__main__':
    solution = Solution()
    assert 3 == solution.minDays([1,10,3,10,2], 3, 1)
    assert -1 == solution.minDays([1,10,3,10,2], 3, 2)
    assert 12 == solution.minDays([7,7,7,7,12,7,7], 2, 3)
    assert 9 == solution.minDays([1,10,2,9,3,8,4,7,5,6], 4, 2)
    assert 93 == solution.minDays([5,37,55,92,22,52,31,62,99,64,92,53,34,84,93,50,28], 8, 2)
    assert 98 == solution.minDays([62,75,98,63,47,65,51,87,22,27,73,92,76,44,13,90,100,85],2,7)
    assert 1000000000 == solution.minDays([1000000000,1000000000], 1, 1)
   