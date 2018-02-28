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


``` java
public class NumMatrix {
    private int[][] sumCol;//we can also do this use sumRow, then use one extra cols
    private int[][] matrix;
    public NumMatrix(int[][] matrix) {
        if (matrix == null || matrix.length == 0) {
            return;
        }
        this.matrix = matrix;
        sumCol = new int[matrix.length + 1][matrix[0].length];
        for (int i = 1; i <= matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                sumCol[i][j] = sumCol[i-1][j] + matrix[i-1][j];
            }
        }
    }
    public void update(int row, int col, int val) {
        for (int i = row + 1; i < sumCol.length; i++) {
            sumCol[i][col] += val - matrix[row][col];
        }
        matrix[row][col] = val;
    }

    public int sumRegion(int row1, int col1, int row2, int col2) {
        int result = 0;
        for (int j = col1; j <= col2; j++) {
            result += sumCol[row2 + 1][j] - sumCol[row1][j];
        }
        return result;
    }
}
```

``` python
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """

        if not matrix:
            return
        self.matrix = matrix
        self.col_sum = [[0] * (len(matrix[0])) for _ in xrange(len(matrix) + 1)]
        for i in xrange(1, len(matrix) + 1):
            for j in xrange(len(matrix[0])):
                self.col_sum[i][j] = self.col_sum[i - 1][j] + self.matrix[i - 1][j]

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        diff = val - self.matrix[row][col]
        for i in xrange(row + 1, len(self.matrix) + 1):
            self.col_sum[i][col] += diff
        self.matrix[row][col] = val

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        ret = 0
        for j in xrange(col1, col2 + 1):
            ret += self.col_sum[row2 + 1][j] - self.col_sum[row1][j]
        return ret
```
