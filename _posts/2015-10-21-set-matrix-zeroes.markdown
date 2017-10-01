---
layout: post
title: 73 - Set Matrix Zeroes
date: 2015-10-21 14:36:15.000000000 -04:00
tags:
- Leetcode
categories:
- Matrix
author: Jason
---
**Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.**


``` java
public class Solution {
    public void setZeroes(int[][] matrix) {
        if (matrix == null || matrix.length == 0) return;
        int row = matrix.length, col = matrix[0].length;
        boolean[] rowZero = new boolean[row];
        boolean[] colZero = new boolean[col];
        for (int i = 0; i < row; i ++) {
            for (int j = 0; j < col; j++) {
                if (matrix[i][j] == 0) {
                    rowZero[i] = true;
                    colZero[j] = true;
                }
            }
        }
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (rowZero[i] || colZero[j]) {
                    matrix[i][j] = 0;
                }
            }
        }
    }O(m + n) space
    public void setZeroes(int[][] matrix) {
        if (matrix == null || matrix.length == 0) return;
        int row = matrix.length, col = matrix[0].length;
        boolean firstRowZero = false, firstColZero = false;
        for (int i = 0; i < row; i++) {
            if (matrix[i][0] == 0) {
                firstColZero = true;
                break;
            }//if first col has zero
        }
        for (int j = 0; j < col; j++) {
            if (matrix[0][j] == 0) {
                firstRowZero = true;
                break;
            }//if first row has zero
        }
        for (int i = 1; i < row; i++) {
            for (int j = 1; j < col; j++) {
                if (matrix[i][j] == 0) {
                    matrix[0][j] = 0;
                    matrix[i][0] = 0;
                }
            }//use first col and first row to store info
        }
        for (int i = 1; i < row; i++) {
            for (int j = 1; j < col; j++) {
                if (matrix[0][j] == 0 || matrix[i][0] == 0){
                    matrix[i][j] = 0;
                }
            }//set elements to zero
        }
        if (firstRowZero) {
            for (int j = 0; j < col; j++) {
                matrix[0][j] = 0;
            }//set first row
        }
        if (firstColZero) {
            for (int i = 0; i < row; i++) {
                matrix[i][0] = 0;
            }//set first col
        }
    }
}//constant space
```

``` python
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        if not matrix:
            return

        zero_row, zero_col = [], []
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_row.append(i)
                    zero_col.append(j)

        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                if i in zero_row or j in zero_col:
                    matrix[i][j] = 0
```

``` python
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        if not matrix:
            return

        row, col = len(matrix), len(matrix[0])
        row_zero, col_zero = False, False

        for j in xrange(col):
            if matrix[0][j] == 0:
                row_zero = True
                break
        for i in xrange(row):
            if matrix[i][0] == 0:
                col_zero = True
                break
        for i in xrange(1, row):
            for j in xrange(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0], matrix[0][j] = 0, 0
        for i in xrange(1, row):
            for j in xrange(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if row_zero:
            for j in xrange(col):
                matrix[0][j] = 0
        if col_zero:
            for i in xrange(row):
                matrix[i][0] = 0
```
