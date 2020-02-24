---
layout: post
title: 57 - Insert Interval
date: 2015-10-21 13:03:18.000000000 -04:00
tags:
- Leetcode
categories:
- Array
author: Jason
---
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary). You may assume that the intervals were initially sorted according to their start times.

``` python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        ret = []
        for interval in intervals:
            if interval[1] < newInterval[0]:
                ret.append(interval)
            elif interval[0] > newInterval[1]:
                ret.append(newInterval)
                newInterval = interval
            else:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
        ret.append(newInterval)
        return ret
```
