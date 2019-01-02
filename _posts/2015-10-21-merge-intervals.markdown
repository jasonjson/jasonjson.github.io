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
class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        intervals.sort(key = lambda x: x.start)
        ret = []
        for interval in intervals:
            if ret and ret[-1].end >= interval.start:
                ret[-1].end = max(ret[-1].end, interval.end)
            else:
                ret.append(interval)
        return ret
```
