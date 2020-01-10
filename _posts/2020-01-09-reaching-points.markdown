---
layout: post
title: 780 - Reaching Points
date: 2020-01-09
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
A move consists of taking a point (x, y) and transforming it to either (x, x+y) or (x+y, y). Given a starting point (sx, sy) and a target point (tx, ty), return True if and only if a sequence of moves exists to transform the point (sx, sy) to (tx, ty). Otherwise, return False.**

```python
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        #First line: if 2 target points are still bigger than 2 starting point, we reduce target points.
        #Second line: check if we reduce target points to (x, y+kx) or (x+ky, y)
        while sx < tx and sy < ty:
            tx, ty = tx % ty, ty % tx
        return sx == tx and sy <= ty and (ty - sy) % sx == 0 or sy == ty and sx <= tx and (tx - sx) % sy == 0
```
