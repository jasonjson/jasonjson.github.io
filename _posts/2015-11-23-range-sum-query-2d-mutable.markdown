---
layout: post
title: Range Sum Query 2D - Mutable
date: 2015-11-23 17:39:50.000000000 -05:00
tags: algorithm
categories:
- Brain teaser
- Matrix
author: Jason
---
<p><strong><em>Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).</em></strong></p>


``` java
public class NumMatrix {
    private int[][] arrs;
    private int[][] Bindex;

    public NumMatrix(int[][] matrix) {
        if (matrix == null || matrix.length == 0) return;
        int row = matrix.length, col = matrix[0].length;
        this.arrs = new int[row][col];
        this.Bindex = new int[row + 1][col + 1];
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                update(i, j, matrix[i][j]);
                arrs[i][j] = matrix[i][j];
            }
        }
    }
    public void update(int row, int col, int val) {
        int diff = val - arrs[row][col];
        arrs[row][col] = val;
        for (int i = row + 1; i < Bindex.length; i += (i & -i)) {
            for (int j = col + 1; j < Bindex[0].length; j += (j & -j)) {
                Bindex[i][j] += diff;
            }
        }
    }
    public int getSum(int row, int col) {
        int sum = 0;
        for (int i = row + 1; i > 0; i -= (i & -i)) {
            for (int j = col + 1; j > 0; j -= (j & -j)) {
                sum += Bindex[i][j];
            }
        }
        return sum;
    }
    public int sumRegion(int row1, int col1, int row2, int col2) {
        return getSum(row2,col2) - getSum(row1-1, col2) - getSum(row2, col1-1) + getSum(row1-1, col1-1);
    }
}
```
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
