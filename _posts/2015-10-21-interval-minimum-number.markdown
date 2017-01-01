---
layout: post
title: Interval Minimum Number
date: 2015-10-21 13:31:18.000000000 -04:00
type: post
published: true
status: publish
categories:
- Subarray
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"bbf9a95630c8d238f326d9ac73190f69";a:2:{s:7:"expires";i:1455274691;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:497;}i:1;a:1:{s:2:"id";i:499;}i:2;a:1:{s:2:"id";i:936;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given an integer array (index from 0 to n-1, where n is the size of this array), and an query list. Each query has two integers [start, end]. For each query, calculate the minimum number between index start and end in the given array, return the result list.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public class SegmentTreeNode {
        int start, end, min;
        SegmentTreeNode left, right;
        public SegmentTreeNode(int start, int end, int min) {
            this.start = start;
            this.end = end;
            this.min = min;
        }
    }    
    public ArrayList<integer> intervalMinNumber(int[] A, ArrayList<interval> queries) {
        ArrayList<integer> result = new ArrayList<integer>();
        if (A ==  null || A.length == 0) return result;
        SegmentTreeNode root = buildTree(A, 0, A.length - 1);
        for (Interval interval : queries) {
            result.add(query(root, interval.start, interval.end));
        }
        return result;
    }
    public SegmentTreeNode buildTree(int[] A, int lo, int hi) {
        if (A == null || A.length == 0 || lo > hi) return null;
        SegmentTreeNode root = new SegmentTreeNode(lo, hi, 0);
        if (lo == hi) {
            root.min = A[lo];
        } else {
            int mid = (lo + hi) / 2;
            root.left = buildTree(A, lo, mid);
            root.right = buildTree(A, mid + 1, hi);
            root.min = Math.min(root.left.min, root.right.min);
        }
        return root;
    }
    public int query(SegmentTreeNode root, int start, int end) {
        if (root == null) return Integer.MAX_VALUE;
        if (root.start == start && root.end == end) {
            return root.min;
        }
        int mid = (root.start + root.end) / 2;
        if (end < mid) {
            return query(root.left, start, end);
        } else if (start > mid) {
            return query(root.right, start, end);
        } else {
            return Math.min(query(root.left, start, mid), query(root.right, mid + 1, end));
        }
    }
}
</integer></integer></interval></integer></pre>
<p>[/expand]</p>
