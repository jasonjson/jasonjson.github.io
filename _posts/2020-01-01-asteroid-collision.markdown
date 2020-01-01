---
layout: post
title: 735 - Asteroid Collision
date: 2020-01-01
tags:
- Leetcode
categories:
- Array
author: Jason
---
**We are given an array asteroids of integers representing asteroids in a row. For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed. Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.**

```python
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if not asteroids:
            return []

        ret = []
        for asteroid in asteroids:
            if not ret or asteroid > 0:
                ret.append(asteroid)
            else:
                while ret and ret[-1] > 0:
                    if ret[-1] == -asteroid:
                        ret.pop()
                        break
                    elif ret[-1] > -asteroid:
                        break
                    elif ret[-1] < -asteroid:
                        ret.pop()
                else:
                    ret.append(asteroid)
        return ret
```
