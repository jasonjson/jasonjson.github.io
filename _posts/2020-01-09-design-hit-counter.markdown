---
layout: post
title: 362 - Design Hit Counter
date: 2020-01-09
tags:
- Leetcode
categories:
- Data Structure
author: Jason
---
Design a hit counter which counts the number of hits received in the past 5 minutes. Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1. It is possible that several hits arrive roughly at the same time.**

```python
from collections import defaultdict
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.times = [0] * 300
        self.counts = [0] * 300

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        index = timestamp % 300
        if self.times[index] != timestamp:
            self.times[index] = timestamp
            self.counts[index] = 1
        else:
            self.counts[index] += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """

        return sum([count for time, count in zip(self.times, self.counts) if time > timestamp - 300])
```
