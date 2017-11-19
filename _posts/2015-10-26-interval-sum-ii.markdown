---
layout: post
title: 207 - Interval Sum II
date: 2015-10-26 11:22:41.000000000 -04:00
tags:
- Lintcode
categories:
- Array
author: Jason
---
**Given an integer array in the construct method, implement two methods query(start, end) and modify(index, value): For query(start, end), return the sum from index start to index end in the given array. For modify(index, value), modify the number in the given index to value**


``` python
class Solution:
    """
    @param: A: An integer array
    """
    def __init__(self, A):
        # do intialization if necessary
        self.root = self.build(A, 0, len(A) - 1)

    def build(self, A, start, end):
        if not A:
            return
        root = SegmentTreeNode(start, end, 0)
        if start == end:
            root.sums = A[start]
        else:
            mid = (start + end) / 2
            root.left = self.build(A, start, mid)
            root.right = self.build(A, mid + 1, end)
            root.sums = root.left.sums + root.right.sums
        return root
    """
    @param: start: An integer
    @param: end: An integer
    @return: The sum from start to end
    """
    def query(self, start, end):
        # write your code here
        return self.query_helper(self.root, start, end)

    def query_helper(self, root, start, end):
        if not root:
            return 0
        if root.start == start and root.end == end:
            return root.sums
        mid = (root.start + root.end) / 2
        if start > mid:
            return self.query_helper(root.right, start, end)
        elif end < mid:
            return self.query_helper(root.left, start, end)
        else:
            return self.query_helper(root.left, start, mid) + self.query_helper(root.right, mid + 1, end)

    """
    @param: index: An integer
    @param: value: An integer
    @return: nothing
    """
    def modify(self, index, value):
        # write your code here
        self.modify_helper(self.root, index, value)

    def modify_helper(self, root, index, value):
        if root.start == index and root.end == index:
            root.sums = value
            return
        mid = (root.start + root.end) / 2
        if index <= mid:
            self.modify_helper(root.left, index, value)
        else:
            self.modify_helper(root.right, index, value)
        root.sums = root.left.sums + root.right.sums
```
