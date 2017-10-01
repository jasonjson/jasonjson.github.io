---
layout: post
title: Interval Sum II
date: 2015-10-26 11:22:41.000000000 -04:00
tags:
- Leetcode
categories:
- Data Structure
author: Jason
---
<p><strong><em>Given an integer array in the construct method, implement two methods query(start, end) and modify(index, value): For query(start, end), return the sum from index start to index end in the given array. For modify(index, value), modify the number in the given index to value</em></strong></p>


``` java
public class Solution {
    class segmentTreeNode {
        int start, end, sum;
        segmentTreeNode left, right;
        segmentTreeNode(int start, int end, int sum) {
            this.start = start;
            this.end = end;
            this.sum = sum;
            left = null;
            right = null;
        }
    }
    
    public segmentTreeNode build(int[] A, int start, int end) {
        if (start > end) return null;
        if (start == end) {
            return new segmentTreeNode(start, start, A[start]);
        }
        segmentTreeNode root = new segmentTreeNode(start, end, 0);
        int mid = (start + end) / 2;
        root.left = build(A, start, mid);
        root.right = build(A, mid + 1, end);
        root.sum = root.left.sum + root.right.sum;
        return root;
    }
    
    private segmentTreeNode root;
    public Solution(int[] A) {
        root = build(A, 0, A.length - 1);
    }

    public long query(int start, int end) {
        return queryHelper(root, start, end);
    }
    public long queryHelper(segmentTreeNode root, int start, int end) {
        if (root == null) return 0;
        if (root.start == start && root.end == end) {
            return root.sum;
        }
        int mid = (root.start + root.end) / 2;
        long leftsum = 0, rightsum = 0;
        if (start <= mid) {
            leftsum = queryHelper(root.left, start, Math.min(mid, end));
        }//注意这里一定要判断mid跟end的大小，不然就没有缩小区间!!
        if (end > mid) {
            rightsum = queryHelper(root.right, Math.max(mid + 1, start), end);
        }//注意这里一定要判断mid + 1跟start的大小，不然就没有缩小区间!!
        return leftsum + rightsum;
    }
    
    public void modify(int index, int value) {
        modifyHelper(root, index, value);
    }
    
    public void modifyHelper(segmentTreeNode root, int index, int value) {
        if (root == null) return;
        if (root.start == index && root.end == index) {
            root.sum = value;
            return;
        }
        int mid = (root.start + root.end) / 2;
        if (root.start <= index && index <= mid) {
            modifyHelper(root.left, index, value);
        } else if (mid < index && index <= root.end) {
            modifyHelper(root.right, index, value);
        }
        root.sum = root.left.sum + root.right.sum;
    }
}
```
