---
layout: post
title: 681 - Next Closest Time
date: 2018-02-28
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused. You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.**


```python
class Solution:
    def nextClosestTime(self, time: str) -> str:

        if not time:
            return ""

        hour, minute = time.split(":")
        hour, minute = int(hour), int(minute)
        while True:
            minute += 1
            if minute == 60:
                hour += 1
                minute = 0
                hour %= 24
            str_hour = "0" + str(hour) if hour <= 9 else str(hour)
            str_min = "0" + str(minute) if minute <= 9 else str(minute)
            new_time = str_hour + ":" + str_min
            if set(new_time) <= set(time):
                return new_time
        return ""
```
