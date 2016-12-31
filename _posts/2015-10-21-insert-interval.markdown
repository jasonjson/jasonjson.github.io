---
layout: post
title: Insert Interval
date: 2015-10-21 13:03:18.000000000 -04:00
type: post
published: true
status: publish
categories:
- Brain teaser
- Data Structure
tags: []
meta:
  _spost_short_title: ''
  _edit_last: '1'
  _wpas_done_all: '1'
  _wpcom_is_markdown: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1468073951;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:457;}i:1;a:1:{s:2:"id";i:560;}i:2;a:1:{s:2:"id";i:497;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a non-overlapping interval list which is sorted by start point. Insert a new interval into it, make sure the list is still in order and non-overlapping (merge intervals if necessary).</em></strong></p>
<p>[expand title="code"]</p>
<pre>
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
</interval></interval></interval></interval></pre>
<p>[/expand]</p>
