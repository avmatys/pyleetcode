from typing import List





class Solution:
    # https://leetcode.com/problems/car-fleet-ii/?envType=problem-list-v2&envId=heap-priority-queue
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:

        def calc_time(i, j):
            return (cars[j][0] - cars[i][0]) / (cars[i][1] - cars[j][1])

        n = len(cars)
        stack = [] # monostack increasing speeds
        res = [-1] * n
        for i in range(n - 1 , -1, -1):
            # Important
            # We check 2 points 
            # - current speed is lesst than a top one - means that we will not collide with next car
            # - check when we will collide with a next car and if we will collide after it collides with next one - pop 
            # cars a b c
            # car b collides car c at moment 5
            # car a collides car b at moment 7 - we will not collide with the next one, but with c
            while stack and (cars[stack[-1]][1] >= cars[i][1] or (res[stack[-1]] > 0 and calc_time(stack[-1], i) > res[stack[-1]])):
                stack.pop()
            if stack:
                res[i] = calc_time(stack[-1], i)
            stack.append(i)
        return res
