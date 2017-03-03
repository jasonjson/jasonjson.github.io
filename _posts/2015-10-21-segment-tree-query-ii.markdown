---
layout: post
title: Segment Tree Query II
date: 2015-10-21 13:30:07.000000000 -04:00
tags: algorithm
categories:
- Data Structure
author: Jason
---
<p><strong><em>For an array, we can build a SegmentTree for it, each node stores an extra attribute count to denote the number of elements in the the array which value is between interval start and end. (The array may not fully filled by elements) Design a query method with three parameters root, start and end, find the number of elements in the in array's interval [start, end] by the given root of value SegmentTree.</em></strong></p>


``` java
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
```
