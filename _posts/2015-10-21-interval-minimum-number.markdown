---
layout: post
title: 205 - Interval Minimum Number
date: 2015-10-21 13:31:18.000000000 -04:00
tags:
- Lintcode
categories:
- Array
author: Jason
---
**Given an integer array (index from 0 to n-1, where n is the size of this array), and an query list. Each query has two integers [start, end]. For each query, calculate the minimum number between index start and end in the given array, return the result list.**


``` java
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
    public ArrayList<Integer> intervalMinNumber(int[] A, ArrayList<interval> queries) {
        ArrayList<Integer> result = new ArrayList<Integer>();
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
```

``` python
class Solution:
    """
    @param: A: An integer array
    @param: queries: An query list
    @return: The result list
    """
    def intervalMinNumber(self, A, queries):
        # write your code here

        root = self.build(A, 0, len(A) - 1)
        return [self.query(root, start, end) for (start, end) in queries]

    def build(self, A, start, end):
        root = SegmentTreeNode(start, end, 0)
        if start == end:
            root.mins = A[start]
        else:
            mid = (start + end) / 2
            root.left = self.build(A, start, mid)
            root.right = self.build(A, mid + 1, end)
            root.mins = min(root.left.mins, root.right.mins)
        return root

    def query(self, root, start, end):
        if not root:
            return 2 ** 31 - 1
        if root.start == start and root.end == end:
            return root.mins
        mid = (root.start + root.end) / 2
        if end < mid:
            return self.query(root.left, start, end)
        elif start > mid:
            return self.query(root.right, start, end)
        else:
            return min(self.query(root.left, start, mid), self.query(root.right, mid + 1, end))
```
