from typing import List, Optional
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

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected


# https://leetcode.com/problems/lru-cache/description
class Node:
     def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_to_head(self, node: Node):
        if node is None:
            return
        if self.head is not None:
            node.next = self.head
            self.head.prev = node 
        if self.tail is None:
            self.tail = node
        self.head = node

    def unlink(self, node: Node):
        if node is None:
            return
        prev_node = node.prev
        next_node = node.next
        if prev_node is not None:
            prev_node.next = next_node
        if next_node is not None:
            next_node.prev = prev_node
        if self.head == node:
            self.head = next_node
        if self.tail == node:
            self.tail = prev_node
        node.prev = None
        node.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity =capacity
        self.cache_map = dict()
        self.history = LinkedList()

    def get(self, key: int) -> int:
        if key not in self.cache_map:
            return -1
        node = self.cache_map[key]
        if self.history.head != node:
            self.history.unlink(node)
            self.history.add_to_head(node)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        self.remove_key(key)
        if len(self.cache_map) >= self.capacity:
            self.remove_least_recent()
        node = Node(key, value)
        self.history.add_to_head(node)
        self.cache_map[key] = node
        
    def remove_key(self, key):
        if key not in self.cache_map:
            return
        node = self.cache_map[key]
        self.history.unlink(node)
        del self.cache_map[key]
        del node

    def remove_least_recent(self):
        if self.history.tail is None:
            return
        self.remove_key(self.history.tail.key)
     

if __name__ == '__main__':
    lru = LRUCache(2)
    lru.put(2, 1)
    lru.put(2, 2)
    assert lru.get(2) == 2
    lru.put(3,3)
    lru.put(4,4)
    assert lru.get(4) == 4
    assert lru.get(2) == -1

    



    
   