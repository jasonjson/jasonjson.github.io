---
layout: post
title: 1011 - Capacity To Ship Packages Within D Days
date: 2020-02-06
tags:
- Leetcode
categories:
- Array
author: Jason
---
A conveyor belt has packages that must be shipped from one port to another within D days. The i-th package on the conveyor belt has a weight of weights[i].  Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship. Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within D days.

```python
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        lo, hi = max(weights), sum(weights)
        while lo < hi:
            mid = (lo + hi) // 2
            if self.is_valid(weights, mid, D):
                hi = mid
            else:
                lo = mid + 1
        return lo

    def is_valid(self, weights, capacity, D):
        curr, days = 0, 1
        for w in weights:
            curr += w
            if curr > capacity:
                curr = w
                days += 1
                if days > D:
                    return False
        return True
```
