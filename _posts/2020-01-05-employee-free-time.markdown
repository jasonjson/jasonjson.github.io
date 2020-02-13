---
layout: post
title: 759 - Employee Free Time
date: 2020-01-05
tags:
- Leetcode
categories:
- Array
author: Jason
---
**We are given a list schedule of employees, which represents the working time for each employee. Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order. Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.**

```python
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        if not schedule:
            return []

        intervals = sorted([i for s in schedule for i in s], key=lambda x: x.start)
        ret, prev = [], intervals[0]
        for interval in intervals[1:]:
            if interval.start <= prev.end:
                prev.end = max(prev.end, interval.end)
            else:
                ret.append(Interval(prev.end, interval.start))
                prev = interval
        return ret
```
