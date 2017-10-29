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


``` java
public class NumMatrix {
    int[][] matrix;
    public NumMatrix(int[][] matrix) {
        if (matrix.length != 0) {
            this.matrix = matrix;
            int row = matrix.length, col = matrix[0].length;
            for (int i = 1; i < row; i++) {
                matrix[i][0] = matrix[i-1][0] + matrix[i][0];
            }
            for (int j = 1; j < col; j++) {
                matrix[0][j] = matrix[0][j-1] + matrix[0][j];
            }
            for (int i = 1; i < row; i++) {
                for (int j = 1; j < col; j++) {
                    matrix[i][j] = matrix[i-1][j] + matrix[i][j-1] - matrix[i-1][j-1] + matrix[i][j];
                }
            }
        }
    }
    public int sumRegion(int row1, int col1, int row2, int col2) {
        if (row1 == 0 && col1 == 0) {
            return matrix[row2][col2];
        } else if (col1 == 0) {
            return matrix[row2][col2] - matrix[row1 - 1][col2];
        } else if (row1 == 0) {
            return matrix[row2][col2] - matrix[row2][col1 - 1];
        }
        return matrix[row2][col2] - matrix[row2][col1 - 1] - matrix[row1 - 1][col2] + matrix[row1 - 1][col1 - 1];
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
        row, col = len(matrix), len(matrix[0])
        self.row_sum = [[0] * (col + 1) for i in xrange(row)]
        for i in xrange(row):
            for j in xrange(1, col + 1):
                self.row_sum[i][j] = self.row_sum[i][j - 1] + matrix[i][j - 1]


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        ret = 0
        for i in xrange(row1, row2 + 1):
            ret += self.row_sum[i][col2 + 1] - self.row_sum[i][col1]
        return ret
```
