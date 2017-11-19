---
layout: post
title: 206 - Interval Sum
date: 2015-10-21 13:31:55.000000000 -04:00
tags:
- Lintcode
categories:
- Array
author: Jason
---
**Given an integer array (index from 0 to n-1, where n is the size of this array), and an query list. Each query has two integers [start, end]. For each query, calculate the sum number between index start and end in the given array, return the result list.**


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

``` python
class Solution:
    """
    @param: A: An integer list
    @param: queries: An query list
    @return: The result list
    """
    def intervalSum(self, A, queries):
        # write your code here
        if not A:
            return

        root = self.build(A, 0, len(A) - 1)
        return [self.query(root, start, end) for (start, end) in queries]


    def build(self, A, start, end):
        root = SegmentTreeNode(start, end, 0)
        if start == end:
            root.sums = A[start]
        else:
            mid = (start + end) / 2
            root.left = self.build(A, start, mid)
            root.right = self.build(A, mid + 1, end)
            root.sums = root.left.sums + root.right.sums
        return root

    def query(self, root, start, end):
        if not root:
            return 0
        if root.start == start and root.end == end:
            return root.sums
        mid = (root.start + root.end) / 2
        if end < mid:
            return self.query(root.left, start, end)
        elif start > mid:
            return self.query(root.right, start, end)
        else:
            return self.query(root.left, start, mid) + self.query(root.right, mid + 1, end)
```
