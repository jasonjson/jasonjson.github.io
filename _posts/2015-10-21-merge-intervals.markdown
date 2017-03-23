---
layout: post
title: Merge Intervals
date: 2015-10-21 13:03:49.000000000 -04:00
tags:
- Algorithm
categories:
- Brain teaser
- Data Structure
author: Jason
---
<p><strong><em>Given a collection of intervals, merge all overlapping intervals.</em></strong></p>


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
        if (intervals.size() == 0) {
            list.add(newInterval);
            return list;
        }
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
