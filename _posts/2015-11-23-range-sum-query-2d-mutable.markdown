---
layout: post
title: 308 - Range Sum Query 2D - Mutable
date: 2015-11-23 17:39:50.000000000 -05:00
tags:
- Leetcode
categories:
- Matrix
author: Jason
---
**Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).**

``` python
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        for row in matrix:
            for i in range(1,len(row)):
                row[i] += row[i - 1]

    def update(self, row: int, col: int, val: int) -> None:
        orig = self.matrix[row][col] - (self.matrix[row][col - 1] if col >= 1 else 0)
        for j in range(col, len(self.matrix[0])):
            self.matrix[row][j] += val - orig

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return sum(self.matrix[i][col2] - (self.matrix[i][col1 - 1] if col1 >= 1 else 0) for i in range(row1, row2 + 1))
```
