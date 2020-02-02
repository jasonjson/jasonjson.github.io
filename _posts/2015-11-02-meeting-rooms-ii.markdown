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


``` java
public class Solution {
    public int minMeetingRooms(Interval[] intervals) {
        if (intervals == null || intervals.length == 0) return 0;
        int max = 1;
        Arrays.sort(intervals, new Comparator<interval>() {
            public int compare (Interval a, Interval b) {
                return a.end - b.end;//sort by finish time
            }
        });
        for (int i = 0; i < intervals.length; i++) {
            int count = 1;//start from 1, since the current meeting also needs one room
            for (int j = i + 1; j < intervals.length; j++) { //j starts at i + 1, otherwise there is no point of sorting
                if (intervals[j].start < intervals[i].end) {
                    count++;
                }
                max = Math.max(max, count);
            }
        }
        return max;
    }
}
```

``` python
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        start = [interval[0] for interval in intervals]
        end = [interval[1] for interval in intervals]
        start.sort()
        end.sort()
        end_index = 0
        room = 0
        for i in range(len(start)):
            if start[i] < end[end_index]:
                room += 1
            else:
                end_index += 1
        return room
```
