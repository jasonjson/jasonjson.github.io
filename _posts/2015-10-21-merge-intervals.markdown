---
layout: post
title: 56 - Merge Intervals
date: 2015-10-21 13:03:49.000000000 -04:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Given a collection of intervals, merge all overlapping intervals.**

``` python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda interval: interval[0])
        ret = []
        for interval in intervals:
            if ret and ret[-1][1] >= interval[0]:
                ret[-1][1] = max(ret[-1][1], interval[1])
            else:
                ret.append(interval)
        return ret
```
