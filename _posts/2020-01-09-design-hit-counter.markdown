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
Design a hit counter which counts the number of hits received in the past 5 minutes (i.e., the past 300 seconds).

Your system should accept a timestamp parameter (in seconds granularity), and you may assume that calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing). Several hits may arrive roughly at the same time.

Implement the HitCounter class:

1. HitCounter() Initializes the object of the hit counter system.
2. void hit(int timestamp) Records a hit that happened at timestamp (in seconds). Several hits may happen at the same timestamp.
3. int getHits(int timestamp) Returns the number of hits in the past 5 minutes from timestamp (i.e., the past 300 seconds).

```python
class HitCounter:

    def __init__(self):
        self.times = [0] * 300
        self.counts = [0] * 300

    def hit(self, timestamp: int) -> None:
        index = timestamp % 300
        if (self.times[index] != timestamp):
            self.times[index] = timestamp
            self.counts[index] = 1
        else:
            self.counts[index] += 1

    def getHits(self, timestamp: int) -> int:
        ret = 0
        for time, count in zip(self.times, self.counts):
            if time > timestamp - 300:
                ret += count
        return ret
```
