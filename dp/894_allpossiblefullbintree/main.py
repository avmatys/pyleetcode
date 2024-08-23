from typing import List
from typing import Optional
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


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __repr__(self):
        result = f"{self.val}"
        if self.left:
            result = f"{result},{self.left}"
        if self.right:
            result = f"{result},{self.right}"

        return result



# https://leetcode.com/problems/all-possible-full-binary-trees/description/
class Solution:

    @timeit
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
        # Full bin tree should contain odd elements
        if n % 2 == 0:
            return []
        
        # Provide memo to avoid additional calculations
        memo = {}
        memo[1] = [TreeNode()]

        def build_subtree(n: int) -> List[Optional[TreeNode]]:
            
            # Current n was previosuly calculated
            if n in memo:
                return memo[n]
            
            # Left and right subtrees can contain up to n-1 elemens. Min count = 1. Step is 2
            result = []
            for i in range(1, n, 2):

                # Build left and right subtrees
                left_subtree = build_subtree(i)
                right_subtree = build_subtree(n-i-1) # n-(n-1) = 1

                # Build all combination of sutrees
                for left in left_subtree:
                    for right in right_subtree:
                        result.append(TreeNode(0, left, right))

            # Store to the memo
            memo[n] = result
            return result
            
        trees = build_subtree(n)
        return trees
    

    def allPossibleFBTDP(self, n: int) -> List[Optional[TreeNode]]:

        # Only odds are ok
        if n % 2 == 0:
            return []

        # Create DP array, where i-th stores all possible trees
        dp = [[] for _ in range(n + 1)]
        dp[1] = [TreeNode()]

        # Iterate through all subtrees from 3 to n
        for tree_size in range(3, n + 1, 2):
            for left_count in range(1, tree_size - 1, 2): 
                right_count = tree_size - left_count - 1 
                # Get previous values for left and right subtrees
                for left in dp[left_count]:
                    for right in dp[right_count]:
                        dp[tree_size].append(TreeNode(0,left,right))

        return dp[n]
    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (3, [[0,0,0]]),
        (7, [[0,0,0,None,None,0,0,None,None,0,0],[0,0,0,None,None,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,None,None,None,None,0,0],[0,0,0,0,0,None,None,0,0]])    
    ]
    
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.allPossibleFBTDP(input), expected)

    
   