---
layout: post
title: Insert Interval
date: 2015-10-21 13:03:18.000000000 -04:00
categories:
- Brain teaser
- Data Structure
author: Jason
---
<p><strong><em>Given a non-overlapping interval list which is sorted by start point. Insert a new interval into it, make sure the list is still in order and non-overlapping (merge intervals if necessary).</em></strong></p>


``` java
class Solution {
    /**
     * Insert newInterval into intervals.
     * @param intervals: Sorted interval list.
     * @param newInterval: A new interval.
     * @return: A new sorted interval list.
     */
    public ArrayList<interval> insert(ArrayList<interval> intervals, Interval newInterval) {
        ArrayList<interval> result = new ArrayList<interval>();
        if (intervals == null || intervals.size() == 0) {
            result.add(newInterval);
            return result;
        }
        for (Interval interval : intervals) {
            if (interval.end < newInterval.start) {
                result.add(interval);
            } else if (interval.start > newInterval.end) {
                result.add(newInterval);
                newInterval = interval;
            } else {
                newInterval = new Interval(Math.min(interval.start, newInterval.start), Math.max(interval.end, newInterval.end));
            }
        }
        result.add(newInterval);
        return result;
    }
}
```
