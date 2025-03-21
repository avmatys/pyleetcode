from typing import List
from datetime import datetime
from typing import Optional
from collections import defaultdict

# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper

class Solution:

    def cook(self, recmap, receipt, supplies, visited):
        if receipt in visited:
            return receipt in supplies
        visited.add(receipt)
        for ing in recmap[receipt]:
            if ing in supplies: 
                continue
            if ing in visited or ing not in recmap.keys():
                return False
            if not self.cook(recmap, ing, supplies, visited):
                return False
        supplies.add(receipt)
        return True


    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        recmap = defaultdict(List)
        for i, rec in enumerate(recipes):
            recmap[rec] = ingredients[i]
        visited, supp = set(), set(supplies)
        result = []
        for rec in recipes:
            if self.cook(recmap, rec, supp, visited):
                result.append(rec)
        return result
            

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected

if __name__ == '__main__':
    solution = Solution()
    assert solution.findAllRecipes(["bread","sandwich","burger"], [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], ["yeast","flour","meat"]) == ["bread","sandwich","burger"]
