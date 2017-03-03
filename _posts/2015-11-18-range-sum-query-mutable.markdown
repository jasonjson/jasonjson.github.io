---
layout: post
title: Range Sum Query - Mutable
date: 2015-11-18 21:19:53.000000000 -05:00
tags: algorithm
categories:
- Data Structure
author: Jason
---
<p><strong><em>Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive. The update(i, val) function modifies nums by updating the element at index i to val.</em></strong></p>


<p><a href="https://www.youtube.com/watch?v=CWDQJGaN1gY">read more</a></p>
``` java
public class NumArray {
    private int[] arrs;
    private int[] BTree;

    public NumArray(int[] nums) {
        this.arrs = new int[nums.length];//wrong: this.arrs = nums;
        this.BTree = new int[nums.length + 1];
        //arrs = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            update(i, nums[i]);//the initial value of arrs[i] is zero, and thus we can update BTree
            arrs[i] = nums[i];//then we assign value to arrs[i],
        }
    }

    public void update(int i, int val) {
        int diff = val - arrs[i];
        arrs[i] = val;
        i++;//the index of Btree is i ++
        while (i < BTree.length) {
            BTree[i] += diff;
            i += i & (-i);//update next value
        }
    }

    public int getSum(int i) {
        i++;
        int sum = 0;
        while (i > 0) {
            sum += BTree[i];
            i -= i & (-i);//add parents
        }
        return sum;
    }

    public int sumRange(int i, int j) {
        return getSum(j) - getSum(i-1);//i - 1 not i
    }
}
```
``` java
public class NumArray {
    segmentTreeNode root;
    public NumArray(int[] nums) {
        this.root = build(nums, 0, nums.length - 1);
    }

    void update(int i, int val) {
        updateNode(root, i, val);
    }

    public int sumRange(int i, int j) {
        return query(root, i, j);
    }

    class segmentTreeNode {
        int start, end, sum;
        segmentTreeNode left, right;
        segmentTreeNode(int start, int end, int sum) {
            this.start = start;
            this.end = end;
            this.sum = sum;
            this.left = null;
            this.right = null;
        }
    }
    public segmentTreeNode build(int[] nums, int start, int end) {
        if (start > end) return null;
        if (start == end) return new segmentTreeNode(start, start, nums[start]);
        int mid = (start + end) / 2;
        segmentTreeNode root = new segmentTreeNode(start, end, 0);
        root.left = build(nums, start, mid);
        root.right = build(nums, mid + 1, end);
        root.sum = root.left.sum + root.right.sum;
        return root;
    }

    public void updateNode(segmentTreeNode root, int i, int val) {
        if (root.start == i && root.end == i) {
            root.sum = val;
            return;
        }
        int mid = (root.start + root.end) / 2;
        if (i <= mid) {
            updateNode(root.left, i, val);
        } else {
            updateNode(root.right, i, val);
        }
        root.sum = root.left.sum + root.right.sum;
    }
    public int query(segmentTreeNode root, int start, int end) {
        if (root.start == start && root.end == end) {
            return root.sum;
        }
        int mid = (root.start + root.end) / 2;
        if (start > mid) {
            return query(root.right, start, end);
        } else if (end <= mid) {
            return query(root.left, start, end);
        } else {
            return query(root.left, start, mid) + query(root.right, mid + 1, end);
        }
    }
}
```
