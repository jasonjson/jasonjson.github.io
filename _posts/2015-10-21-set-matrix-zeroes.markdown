---
layout: post
title: Set Matrix Zeroes
date: 2015-10-21 14:36:15.000000000 -04:00
categories:
- Matrix
author: Jason
---
<p><strong><em>Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.</em></strong></p>


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
