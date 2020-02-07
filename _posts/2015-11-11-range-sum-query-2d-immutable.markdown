---
layout: post
title: 304 - Range Sum Query 2D - Immutable
date: 2015-11-11 22:02:59.000000000 -05:00
tags:
- Leetcode
categories:
- Matrix
author: Jason
---
**Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by (row1, col1), (row2, col2).**

``` python
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        for row in self.matrix:
            for i in range(1, len(row)):
                row[i] += row[i - 1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ret = 0
        for i in range(row1, row2 + 1):
            ret += self.matrix[i][col2] - (self.matrix[i][col1 - 1] if col1 > 0 else 0)
        return ret
```
