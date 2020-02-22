---
layout: post
title: 253 - Meeting Rooms II
date: 2015-11-02 07:46:53.000000000 -05:00
tags:
- Leetcode
categories:
- Sorting
author: Jason
---
**Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si &lt; ei), find the minimum number of conference rooms required.**

``` python
from heapq import heappush, heapreplace
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])
        heap = []
        for interval in intervals:
            if heap and interval[0] >= heap[0]:
                heapreplace(heap, interval[1])
            else:
                heappush(heap, interval[1])
        return len(heap)
```
