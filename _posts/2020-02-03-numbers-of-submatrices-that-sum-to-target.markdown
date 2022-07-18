---
layout: post
title: 1074 - Numbers Of Submatrices That Sum To Target
date: 2020-02-03
tags:
- Leetcode
categories:
- Matrix
author: Jason
---
Given a matrix and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

```python
from collections import defaultdict
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        for row in matrix:
            for j in range(1, len(row)):
                row[j] += row[j - 1]
        ret = 0
        for i in range(len(matrix[0])):
            for j in range(i, len(matrix[0])):
                s_dict = defaultdict(int)
                curr, s_dict[0] = 0, 1
                for row in matrix:
                    curr += row[j] - (row[i - 1] if i > 0 else 0)
                    ret += s_dict[curr - target]
                    s_dict[curr] += 1
        return ret
```
