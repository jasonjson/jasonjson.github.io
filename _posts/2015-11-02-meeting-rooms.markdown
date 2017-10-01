---
layout: post
title: Meeting Rooms
date: 2015-11-02 07:36:10.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
<p><strong><em>Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si &lt; ei), determine if a person could attend all meetings.</em></strong></p>


``` java
public class Solution {
    public boolean canAttendMeetings(Interval[] intervals) {
        if (intervals == null || intervals.length == 0) return true;
        
        Arrays.sort(intervals, new Comparator<interval>() {
            public int compare (Interval a, Interval b) {
                return a.start - b.start;
            }
        });
        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i].start < intervals[i-1].end) {
                return false;
            }
        }
        return true;
    }
}
```
