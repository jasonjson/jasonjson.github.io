---
layout: post
title: 981 - Time Based Key Value Store
date: 2019-12-27
tags:
- Leetcode
categories:
- Sort
author: Jason
---

```python
from collections import defaultdict
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pair = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.pair[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.pair:
            return ""
        values = self.pair[key]
        lo, hi = 0, len(values) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if values[mid][1] == timestamp:
                return values[mid][0]
            elif values[mid][1] < timestamp:
                if values[mid + 1][1] > timestamp:
                    return values[mid][0]
                lo = mid + 1
            else:
                hi = mid - 1
        return values[lo][0] if values[lo][1] <= timestamp else ""
```
