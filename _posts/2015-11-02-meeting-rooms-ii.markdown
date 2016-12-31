---
layout: post
title: Meeting Rooms II
date: 2015-11-02 07:46:53.000000000 -05:00
type: post
published: true
status: publish
categories:
- Brain teaser
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1468873105;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1242;}i:1;a:1:{s:2:"id";i:109;}i:2;a:1:{s:2:"id";i:560;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si &lt; ei), find the minimum number of conference rooms required.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
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
</interval></pre>
<p>[/expand]</p>
<p>[expand title = "O(n) time and O(n) space"]</p>
<pre>
public class Solution {
    public int minMeetingRooms(Interval[] intervals) {
        if (intervals == null || intervals.length == 0) return 0;
        
        Arrays.sort(intervals, new Comparator<interval>() {
           public int compare (Interval a, Interval b) {
               return a.start - b.start;
           } 
        });
        PriorityQueue<integer> pq = new PriorityQueue<integer>();
        for (Interval interval : intervals) {
            if (!pq.isEmpty() && interval.start >= pq.peek()) {
                pq.poll();//可以想象把pq.peek()和新的interval合并在一起
            }
            pq.offer(interval.end);
        }
        return pq.size();
    }
}
</integer></integer></interval></pre>
<p>[/expand]</p>
