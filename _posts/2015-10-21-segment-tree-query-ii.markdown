---
layout: post
title: Segment Tree Query II
date: 2015-10-21 13:30:07.000000000 -04:00
type: post
published: true
status: publish
categories:
- Data Structure
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1466014006;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:488;}i:1;a:1:{s:2:"id";i:1030;}i:2;a:1:{s:2:"id";i:499;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>For an array, we can build a SegmentTree for it, each node stores an extra attribute count to denote the number of elements in the the array which value is between interval start and end. (The array may not fully filled by elements) Design a query method with three parameters root, start and end, find the number of elements in the in array's interval [start, end] by the given root of value SegmentTree.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public int query(SegmentTreeNode root, int start, int end) {
        if (root == null) return 0;
        if (start > end) return 0;
        start = Math.max(root.start, start);
        end = Math.min(root.end, end);//for query out of bound
        if (root.start == start && root.end == end) return root.count;
        int mid = (root.start + root.end) / 2;
        if (start > mid) {
            return query(root.right, start, end);
        } else if (end < mid) {
            return query(root.left, start, end);
        } else {
            return query(root.left, start, mid) + query(root.right, mid + 1, end);
        }
    }
}
</pre>
<p>[/expand]</p>
