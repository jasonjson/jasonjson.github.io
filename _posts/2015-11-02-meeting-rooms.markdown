---
layout: post
title: 252 - Meeting Rooms
date: 2015-11-02 07:36:10.000000000 -05:00
tags:
- Leetcode
categories:
- Array
author: Jason
---
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

``` python
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        prev = None
        for interval in intervals:
            if prev and prev[1] > interval[0]:
                return False
            else:
                prev = interval
        return True
```
