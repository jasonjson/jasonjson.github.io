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
Given a matrix, and a target, return the number of non-empty submatrices that sum to target.

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
                for k in range(len(matrix)):
                    curr += matrix[k][j] - (matrix[k][i - 1] if i > 0 else 0)
                    ret += s_dict[curr - target]
                    s_dict[curr] += 1
        return ret
```
