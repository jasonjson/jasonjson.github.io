---
layout: post
title: 363 - Max Sum Of Rectangle No Larger Than K
date: 2020-02-05
tags:
- Leetcode
categories:
- Matrix
author: Jason
---
Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that its sum is no larger than k.

```python
from bisect import bisect_left, insort
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        for row in matrix:
            for i in range(1, len(row)):
                row[i] += row[i - 1]

        ret = -float("inf")
        for j in range(len(matrix[0])):
            for l in range(j, len(matrix[0])):
                sums, curr = [0], 0
                for i in range(len(matrix)):
                    curr += matrix[i][l] - (matrix[i][j - 1] if j > 0 else 0)
                    i = bisect_left(sums, curr - k)
                    if i < len(sums):
                        ret = max(ret, curr - sums[i])
                    insort(sums, curr)
        return ret
```
