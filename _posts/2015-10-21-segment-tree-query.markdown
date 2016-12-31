---
layout: post
title: Segment Tree Query
date: 2015-10-21 13:29:33.000000000 -04:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1453082467;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:492;}i:1;a:1:{s:2:"id";i:936;}i:2;a:1:{s:2:"id";i:499;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>For an integer array (index from 0 to n-1, where n is the size of this array), in the corresponding SegmentTree, each node stores an extra attribute max to denote the maximum number in the interval of the array (index from start to end). Design a query method with three parameters root, start and end, find the maximum number in the interval [start, end] by the given root of segment tree.</em></strong></p>
<p>[expand title="code1"]</p>
<pre>
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
</pre>
<p>[/expand]</p>
<p>[expand title = "code2"]</p>
<pre>
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
</pre>
<p>[/expand]<br />
[expand title = "code3"]</p>
<pre>
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
</pre>
<p>[/expand]</p>
