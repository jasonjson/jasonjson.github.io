---
layout: post
title: 365 - Water And Jug Problem
date: 2017-11-07
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly z litres using these two jugs. If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end. Operations allowed:**
* Fill any of the jugs completely with water.
* Empty any of the jugs.
* Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.


```python
class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if x + y < z:
            return False
        elif x == z or y == z or x + y == z:
            return True
        else:
            return z % self.gcd(x, y) == 0

    def gcd(self, x, y):
        while y:
            x, y = y, x % y
        return x
```
