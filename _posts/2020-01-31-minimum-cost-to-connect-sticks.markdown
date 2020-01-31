---
layout: post
title: 1167 - Minimum Cost To Connect Sticks
date: 2020-01-31
tags:
- Leetcode
categories:
- Array
author: Jason
---
You have some sticks with positive integer lengths. You can connect any two sticks of lengths X and Y into one stick by paying a cost of X + Y.  You perform this action until there is one stick remaining. Return the minimum cost of connecting all the given sticks into one stick in this way.

```python
from heapq import heapify, heappush, heappop
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        ret = 0
        heapify(sticks)
        while len(sticks) > 1:
            m1, m2 = heappop(sticks), heappop(sticks)
            new_stick = m1 + m2
            heappush(sticks, new_stick)
            ret += new_stick
        return ret
```
