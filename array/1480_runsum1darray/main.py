from typing import List

class Solution:

    def runningSum(self, nums: List[int]) -> List[int]:
        result = nums.copy()
        for i in range(1, len(nums)):
            result[i] = result[i-1] + result[i]    
        return result
    
    def runningSumInPlace(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] + nums[i]    
        return nums
    
    
if __name__ == '__main__':
    solution = Solution()
    assert [1,3,6,10] == solution.runningSum([1,2,3,4])
    assert [1] == solution.runningSum([1])
    assert [3,4,6,16,17] == solution.runningSum([3,1,2,10,1])

   