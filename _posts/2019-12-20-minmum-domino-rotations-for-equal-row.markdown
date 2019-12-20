---
layout: post
title: 1007 - Minmum Domino Rotations For Equal Row
date: 2019-12-20
tags:
- Leetcode
categories:
- Array
author: Jason
---
**In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.) We may rotate the i-th domino, so that A[i] and B[i] swap values. Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same. If it cannot be done, return -1.**

```python
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        if not A or not B:
            return -1

        count_a = [0] * 7
        count_b = [0] * 7
        count_share = [0] * 7
        for a, b in zip(A, B):
            count_a[a] += 1
            count_b[b] += 1
            if a == b:
                count_share[a] += 1

        ret = []
        for i in range(1, 7):
            if count_a[i] + count_b[i] - count_share[i] == len(A):
                ret.append(min(count_a[i], count_b[i]) - count_share[i])
        return min(ret) if ret else -1
```
