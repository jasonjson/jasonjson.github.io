---
layout: post
title: 307 - Range Sum Query - Mutable
date: 2015-11-18 21:19:53.000000000 -05:00
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive. The update(i, val) function modifies nums by updating the element at index i to val.**


```java
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

```python
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.sums = [0]
        for num in nums:
            self.sums.append(self.sums[-1] + num)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        diff = val - self.nums[i]
        self.nums[i] = val
        for j in xrange(i + 1, len(self.sums)):
            self.sums[j] += diff

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums[j + 1] - self.sums[i]
```

```python
class SegmentNode(object):

    def __init__(self, lo, hi, sums):
        self.lo = lo
        self.hi = hi
        self.sums = sums
        self.left = None
        self.right = None

class NumArray(object):

    def __init__(self, nums):
        self.root = self.build(0, len(nums) - 1, nums)

    def build(self, lo, hi, nums):
        if lo > hi:
            return
        elif lo == hi:
            return SegmentNode(lo, hi, nums[lo])
        else:
            mid = (lo + hi) / 2
            root = SegmentNode(lo, hi, 0)
            root.left = self.build(lo, mid, nums)
            root.right = self.build(mid + 1, hi, nums)
            root.sums = root.left.sums + root.right.sums
            return root

    def update(self, i, val):
        self.update_node(self.root, i, val)

    def update_node(self, node, i, val):
        if node.lo == i and node.hi == i:
            node.sums = val
        else:
            mid = (node.lo + node.hi) / 2
            if i <= mid:
                self.update_node(node.left, i, val)
            else:
                self.update_node(node.right, i, val)
            node.sums = node.left.sums + node.right.sums


    def sumRange(self, i, j):
        return self.sum_node(self.root, i, j)

    def sum_node(self, node, i, j):
        if node.lo == i and node.hi == j:
            return node.sums
        mid = (node.lo + node.hi) / 2
        if j <= mid:
            return self.sum_node(node.left, i, j)
        elif i > mid:
            return self.sum_node(node.right, i, j)
        else:
            return self.sum_node(node.left, i, mid) + self.sum_node(node.right, mid + 1, j)
```
