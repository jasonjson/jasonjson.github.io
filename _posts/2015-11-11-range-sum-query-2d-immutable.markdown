---
layout: post
title: Range Sum Query 2D - Immutable
date: 2015-11-11 22:02:59.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
- Matrix
author: Jason
---
<p><strong><em>Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by (row1, col1), (row2, col2).</em></strong></p>


``` java
public class NumMatrix {
    private int[][] matrix;
    private int[][] sumRow; //sumRow or sumCol, extra col for sumRow, extra row for sumCol
    public NumMatrix(int[][] matrix) {
        if (matrix == null || matrix.length == 0) return;
        
        this.matrix = matrix;
        sumRow = new int[matrix.length][matrix[0].length + 1];
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 1; j <= matrix[0].length; j++) {
                sumRow[i][j] = sumRow[i][j-1] + matrix[i][j-1];
            }
        }
    }
    public int sumRegion(int row1, int col1, int row2, int col2) {
        int result = 0;
        for (int i = row1; i <= row2; i++) {
            result += sumRow[i][col2 + 1] - sumRow[i][col1];
            //remember the col size of sumRow, we want to include both the value at col1 and col2
        }
        return result;
    }
}
```
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
