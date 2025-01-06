from typing import List
from datetime import datetime
import random

# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper

# https://leetcode.com/problems/insert-delete-getrandom-o1/description/
class RandomizedSet:

    def __init__(self):
        self.val_idx = {}
        self.values = []
        pass

    def insert(self, val: int) -> bool:
        if val in self.val_idx:
            return False
        self.values.append(val)
        self.val_idx[val] = len(self.values) - 1
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.val_idx:
            return False
        arr_idx = self.val_idx[val]
        self.values[arr_idx] = self.values[-1]
        self.val_idx[self.values[-1]] = arr_idx
        self.values.pop()
        del self.val_idx[val]
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.values)



if __name__ == '__main__':
    solution = RandomizedSet()
    assert True  == solution.insert(1)
    assert True  == solution.insert(2)
    assert True  == solution.insert(3)
    assert False  == solution.insert(1)   
    assert False  == solution.remove(4)  
    assert True  == solution.remove(1)  
    assert True  == solution.remove(2)   
    assert True  == solution.remove(3)  
    assert True  == solution.insert(1)
    assert True  == solution.insert(2)
    assert True  == solution.insert(3)
    assert True  == solution.remove(2)   
    assert True  == solution.remove(3) 
    assert 1 == solution.getRandom()
    
   