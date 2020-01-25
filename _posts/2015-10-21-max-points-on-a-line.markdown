---
layout: post
title: 149 - Max Points on a Line
date: 2015-10-21 14:29:12.000000000 -04:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.**

``` python
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return len(points)

        ret = 0
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue
                (x1, y1), (x2, y2) = points[i], points[j]
                count = 0
                if points[i] == points[j]:
                    for point in points:
                        if points[i] == point:
                            count += 1
                else:
                    for x3, y3 in points:
                        if (x3 - x1) * (y2 - y1) == (x2 - x1) * (y3 - y1):
                            count += 1
                ret = max(ret, count)
        return ret
```
