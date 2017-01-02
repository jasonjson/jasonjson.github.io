---
layout: post
title: Segment Tree Query
date: 2015-10-21 13:29:33.000000000 -04:00
categories:
- Data Structure
author: Jason
---
<p><strong><em>For an integer array (index from 0 to n-1, where n is the size of this array), in the corresponding SegmentTree, each node stores an extra attribute max to denote the maximum number in the interval of the array (index from start to end). Design a query method with three parameters root, start and end, find the maximum number in the interval [start, end] by the given root of segment tree.</em></strong></p>


``` java
public class Solution {
    /**
     *@param root, start, end: The root of segment tree and 
     *                         an segment / interval
     *@return: The maximum number in the interval [start, end]
     */
    public int query(SegmentTreeNode root, int start, int end) {
        // write your code here
        if (root == null || start > end) return -1;
        
        if (root.start == start && root.end == end) {
            return root.max;
        } 
        int mid = (root.start + root.end) / 2;
        if (end < mid) {//max is in left subtree, no <=
            return query(root.left, start, end);
        } else if (start > mid) {//max is in right subtree, no >=
            return query(root.right, start, end);
        } else {//can be in left tree or right tree
            return Math.max(query(root.left, start, mid), query(root.right, mid + 1,  end));
        }
    }
}
```
``` java
public class Solution {
    /**
     *@param root, start, end: The root of segment tree and 
     *                         an segment / interval
     *@return: The maximum number in the interval [start, end]
     */
    public int query(SegmentTreeNode root, int start, int end) {
        if (root == null) {
            return Integer.MIN_VALUE;
        }
        if (root.start == start && root.end == end) {
            return root.max;
        }
        int mid = (root.start + root.end) / 2;
        int leftMax = Integer.MIN_VALUE, rightMax = Integer.MIN_VALUE;
        if (start <= mid) {
            leftMax = query(root.left, start, Math.min(mid, end));
        }
        if (mid < end) {
            rightMax = query(root.right, Math.max(mid + 1, start), end);
        }
        return Math.max(leftMax, rightMax);
    }
}
```

``` java
public class Solution {
    public int query(SegmentTreeNode root, int start, int end) {
        // write your code here
        if (root == null || start > root.end || end < root.start) { 
            return Integer.MIN_VALUE;
        }
        if (root.start == root.end) {
            return root.max;
        } else {
            return Math.max(query(root.left, start, end), query(root.right, start, end));
        }
    }
}
```
