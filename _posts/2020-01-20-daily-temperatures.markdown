---
layout: post
title: 739 - Daily Temperatures
date: 2020-01-20
tags:
- Leetcode
categories:
- Array
author: Jason
---
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

```python
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if not T:
            return []

        ret = [0] * len(T)
        stack = []
        for i in range(len(T)):
            while stack and T[stack[-1]] < T[i]:
                index = stack.pop()
                ret[index] = max(i - index, 0)
            stack.append(i)
        return ret
```
