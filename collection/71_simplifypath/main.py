from typing import List
from datetime import datetime
import math

# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper

# https://leetcode.com/problems/simplify-path/
class Solution:

    @timeit
    def simplifyPath(self, path: str) -> str:
        dirs = []
        n = len(path)
        i = 0
        while i < n:
            if path[i] == '/':
                i += 1
            elif path[i] == '.':
                dir_len = 1
                while i + dir_len < n and path[i + dir_len] != '/':
                    dir_len += 1
                if dir_len == 2 and path[i + 1] == '.':
                    if dirs:
                        dirs.pop()
                elif dir_len != 1:
                    dirs.append(path[i : i + dir_len])
                i += dir_len
            else:
                dir_len = 1
                while i + dir_len < n and path[i + dir_len] != '/':
                    dir_len += 1
                dirs.append(path[i : i + dir_len])
                i += dir_len
        return "/" + "/".join(dirs)
    
    @timeit
    def simplifyPath2(self, path: str) -> str:
        subpaths = path.split("/")
        dirs = []
        for subpath in subpaths:
            if subpath == "" or subpath == ".":
                continue
            if subpath == "..":
                if dirs:
                    dirs.pop()
            else:
                dirs.append(subpath)
        return "/" + "/".join(dirs)
        

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ("/..hidden", "/..hidden"),
        ("/hello../world", "/hello../world"),
        ("/../..ga/b/.f..d/..../e.baaeeh./.a", "/..ga/b/.f..d/..../e.baaeeh./.a"),
        ("/.../a/../b/c/../d/./", "/.../b/d"),
        ("/home/../", "/"),
        ("/../", "/"),
        ("/home/user/./Downloads/../Pictures/././", "/home/user/Pictures"),
        ("/", "/"),
        ("/home/user/Documents/../../../usr/local/bin", "/usr/local/bin"),
        ("/a//b//c//////d", "/a/b/c/d"),
        ("/a/..", "/"),
        ("/a/../", "/"),
        ("/a/./b/../../c/", "/c"),
        ("/abc/...", "/abc/...")
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.simplifyPath2(input), expected)


    
   