---
layout: post
title: 1231 - Divide Chocolate
date: 2020-02-03
tags:
- Binary Search, Greedy
categories:
- Array
author: Jason
---

```python
class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        lo, hi = min(sweetness), sum(sweetness)
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.is_valid(sweetness, K, mid):
                hi = mid - 1
                #1) divide the array into m parts and each part is larger than mid
                #2) fail to divide into m parts
            else:
                lo = mid + 1
        return lo

    def is_valid(self, sweetness, K, target):
        curr, count = 0, 1
        for s in sweetness:
            curr += s
            if curr > target:
                curr = 0
                count += 1
                if count > K + 1:
                    return False
        return True
```
