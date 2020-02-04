---
layout: post
title: 939 - Minimum Area Rectangle
date: 2020-02-04
tags:
- Leetcode
categories:
- Array
author: Jason
---
Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes. If there isn't any rectangle, return 0.

```python
from collections import defaultdict
from itertools import combinations
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        same_x = defaultdict(set)
        for x, y in points:
            same_x[x].add(y)

        ret = float("inf")
        for x1, x2 in combinations(same_x, 2):
            same_y = same_x[x1] & same_x[x2]
            if len(same_y) >= 2:
                for y1, y2 in combinations(same_y, 2):
                    ret = min(ret, abs(x1 - x2) * abs(y1 - y2))
        return ret if ret != float("inf") else 0
```
