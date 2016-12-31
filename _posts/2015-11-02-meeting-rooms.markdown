---
layout: post
title: Meeting Rooms
date: 2015-11-02 07:36:10.000000000 -05:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1467816954;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1244;}i:1;a:1:{s:2:"id";i:560;}i:2;a:1:{s:2:"id";i:488;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si &lt; ei), determine if a person could attend all meetings.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
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
</interval></pre>
<p>[/expand]</p>
