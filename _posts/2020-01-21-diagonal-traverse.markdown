---
layout: post
title: 498 - Diagonal Traverse
date: 2020-01-21
tags:
- Leetcode
categories:
- Array
author: Jason
---
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

```python
from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        diag_nums = defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                diag_nums[i + j].append(matrix[i][j])
        ret = []
        for k in range(len(matrix) + len(matrix[0]) - 1):
            if k % 2 == 0:
                diag_nums[k].reverse()
            ret.extend(diag_nums[k])
        return ret
```
