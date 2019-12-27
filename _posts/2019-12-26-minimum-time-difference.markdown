---
layout: post
title: 539 - Minimum Time Difference
date: 2019-12-26
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.**

```python
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        def to_min(time):
            return 60 * int(time[:2]) + int(time[3:])

        mins = sorted((map(to_min, timePoints)))
        mins.append(60 * 24 + mins[0])
        return min([b - a for a, b in zip(mins, mins[1:])])
```
