---
layout: post
title: 973 - K Closest Points To Origin
date: 2020-02-10
tags:
- Leetcode
categories:
- Array
author: Jason
---
We have a list of points on the plane.  Find the K closest points to the origin (0, 0). You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

```python
from heapq import heappush, heappop
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        ret = []
        for p in points:
            heappush(ret, (-p[0] ** 2 - p[1] ** 2, p))
            if len(ret) > K:
                heappop(ret)
        return [p for _, p in ret]
```
