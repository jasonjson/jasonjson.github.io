---
layout: post
title: 528 - Random Pick With Weight
date: 2020-01-18
tags:
- Leetcode
categories:
- Array
author: Jason
---
Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

```python
from random import randint
class Solution:
    def __init__(self, w: List[int]):
        self.weight = []
        s = 0
        for weight in w:
            s += weight
            self.weight.append(s)

    def pickIndex(self) -> int:
        target = randint(1, self.weight[-1])
        lo, hi = 0, len(self.weight) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.weight[mid] == target:
                return mid
            elif self.weight[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo
```
