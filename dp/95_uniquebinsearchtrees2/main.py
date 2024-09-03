from typing import List
from typing import Optional
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

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/unique-binary-search-trees-ii/description
class Solution:

    @timeit
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
       
        # Dict to store possbile subtrees for a combination (start, end)
        cache = {}
        def generate_subtree(start: int, end: int):
           
            # Base case when we can't create a new TreeNode from given start and end
            res = []
            if start > end:
                res.append(None)
                return res
            
            # Probablu we have already calculated subtrees for the combination of start and end
            subtree_key = (start, end)
            if subtree_key in cache:
                return cache[subtree_key]
            

            # Calculate left and right subtrees
            for i in range(start, end + 1):
                
                left_subtrees = generate_subtree(start, i - 1)
                right_subtrees = generate_subtree(i + 1, end)

                # Combine subtrees
                for left in left_subtrees:
                    for right in right_subtrees:
                        node = TreeNode(i, left, right)
                        res.append(node)
                
            # Store result in cache
            cache[subtree_key] = res

            return res

        subtress = generate_subtree(1, n)
        return subtress


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (3, [[1,None,2,None,3],[1,None,3,2],[2,1,3],[3,1,None,None,2],[3,2,None,1]])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.generateTrees(input), expected)

    
   