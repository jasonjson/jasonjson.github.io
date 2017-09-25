---
layout: post
title: Merge Intervals
date: 2015-10-21 13:03:49.000000000 -04:00
tags:
- Algorithm
categories:
- Brain teaser
author: Jason
---
**Given a collection of intervals, merge all overlapping intervals.**


``` java
class Solution {
    /**
     * @param intervals: Sorted interval list.
     * @return: A new sorted interval list.
     */
    public List<interval> merge(List<interval> intervals) {
        // write your code here
        List<interval> result = new ArrayList<interval>();
        if (intervals == null || intervals.size() == 0) return result;

        for (Interval interval : intervals) {
            result = helper(result, interval);
        }
        return result;
    }

    public List<interval> helper(List<interval> intervals, Interval newInterval) {
        List<interval> list = new ArrayList<interval>();
        for (Interval interval : intervals) {
            if (interval.end < newInterval.start) {
                list.add(interval);
            } else if (interval.start > newInterval.end) {
                list.add(newInterval);
                newInterval = interval;
            } else {
                newInterval = new Interval(Math.min(interval.start, newInterval.start), Math.max(interval.end, newInterval.end));
            }
        }
        list.add(newInterval);
        return list;
    }
}
```

``` python
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        if not intervals:
            return []

        ret = []
        for interval in intervals:
            ret = self.helper(ret, interval)
        return ret

    def helper(self, curr, new_interval):
        ret = []
        for interval in curr:
            if interval.end < new_interval.start:
                ret.append(interval)
            elif interval.start > new_interval.end:
                ret.append(new_interval)
                new_interval = interval
            else:
                new_interval = Interval(min(interval.start, new_interval.start), max(interval.end, new_interval.end))
        ret.append(new_interval)
        return ret
```
