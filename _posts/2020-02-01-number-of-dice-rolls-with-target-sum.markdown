---
layout: post
title: 1155 - Number Of Dice Rolls With Target Sum
date: 2020-02-01
tags:
- Leetcode
categories:
- Dynamic Programming
author: Jason
---
You have d dice, and each die has f faces numbered 1, 2, ..., f. Return the number of possible ways (out of fd total ways) modulo 10^9 + 7 to roll the dice so the sum of the face up numbers equals target.

``` python
from functools import lru_cache
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        @lru_cache(None)
        def count(num, sums):
            if num == 0:
                return 1 if sums == 0 else 0
            return sum(count(num - 1, i) for i in range(max(0, sums - f), sums))
        return count(d, target) % (10 ** 9 + 7)
```
