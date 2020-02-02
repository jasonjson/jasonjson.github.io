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

```python
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        cache = {}
        def count(d, t):
            if d == 0:
                return 1 if t == 0 else 0
            elif (d, t) in cache:
                return cache[(d, t)]
            ways = sum(count(d - 1, i) for i in range(max(0, t - f), t))
            cache[(d, t)] = ways
            return ways

        return count(d, target) % (10 ** 9 + 7)
```
