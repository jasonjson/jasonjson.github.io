---
layout: post
title: 986 - Interval List Intersections
date: 2020-01-18
tags:
- Leetcode
categories:
- Array
author: Jason
---
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order. Return the intersection of these two interval lists.
(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

```python
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not B:
            return []

        i = j = 0
        ret = []
        while i < len(A) and j < len(B):
            if A[i][1] < B[j][0]:
                i += 1
            elif B[j][1] < A[i][0]:
                j += 1
            else:
                ret.append([max(A[i][0], B[j][0]), min(A[i][1], B[j][1])])
                if A[i][1] > B[j][1]:
                    j += 1
                else:
                    i += 1
        return ret
```
