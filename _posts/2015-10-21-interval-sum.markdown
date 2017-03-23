---
layout: post
title: Interval Sum
date: 2015-10-21 13:31:55.000000000 -04:00
tags:
- Algorithm
categories:
- Subarray
author: Jason
---
<p><strong><em>Given an integer array (index from 0 to n-1, where n is the size of this array), and an query list. Each query has two integers [start, end]. For each query, calculate the sum number between index start and end in the given array, return the result list.</em></strong></p>


``` java
public class Solution {
    public class SegmentTreeNode {
        int start, end;
        long sum;
        SegmentTreeNode left, right;
        public SegmentTreeNode (int start, int end, long sum) {
            this.start = start;
            this.end = end;
            this.sum = sum;
        }
    }
    public ArrayList<long> intervalSum(int[] A, ArrayList<interval> queries) {
        ArrayList<long> result = new ArrayList<long>();
        if (A == null || A.length == 0) return result;
        SegmentTreeNode root = buildTree(A, 0, A.length - 1);
        for (Interval interval : queries) {
            result.add(query(root, interval.start, interval.end));
        }
        return result;
    }
    public SegmentTreeNode buildTree(int[] A, int start, int end) {
        if (A == null || start > end) return null;
        
        SegmentTreeNode root = new SegmentTreeNode(start, end, 0);
        if(start == end) {
            root.sum = A[start];
        } else {
            int mid = (start + end) / 2;
            root.left = buildTree(A, start, mid);
            root.right = buildTree(A, mid + 1, end);
            root.sum = root.left.sum + root.right.sum;
        }
        return root;
    }
    public long query(SegmentTreeNode root, int lo, int hi) {
        if (root == null) return 0;
        if (root.start == lo && root.end == hi) {
            return root.sum;
        }
        int mid = (root.start + root.end) / 2;//bug!!! root.start + root.end, not lo + hi
        if (hi < mid) {
            return query(root.left, lo, hi);
        } else if (lo > mid) {
            return query(root.right, lo, hi);
        } else {
            return query(root.left, lo, mid) + query(root.right, mid + 1, hi);
        }
    }
}
```
