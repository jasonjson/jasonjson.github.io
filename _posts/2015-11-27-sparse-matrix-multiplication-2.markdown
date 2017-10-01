---
layout: post
title: Sparse Matrix Multiplication
date: 2015-11-27 19:09:59.000000000 -05:00
tags:
- Leetcode
categories:
- Matrix
author: Jason
---
<p><strong><em>Given two sparse matrices A and B, return the result of AB.</em></strong></p>

<a href="http://www.cs.cmu.edu/~scandal/cacm/node9.html">read more</a></p>

``` java
public class Solution {
    public int[][] multiply(int[][] A, int[][] B) {
        if (A.length == 0 || B.length == 0) return new int[][]{};
        
        int row = A.length, col = B[0].length, mid = B.length;
        List<List<integer>> temp = new ArrayList<List<integer>>();
        for (int i = 0; i < row; i++) {
            List<integer> list = new ArrayList<>();
            for (int j = 0; j < mid; j++) {
                if (A[i][j] != 0) {
                    list.add(j);
                    list.add(A[i][j]);
                }
            }
            temp.add(list);
        }
        int[][] result = new int[row][col];
        for (int i = 0; i < row; i++) {
            List<integer> list = temp.get(i);
            for (int l = 0; l + 1 < list.size(); l += 2) {
                int colNum = list.get(l);
                int colVal = list.get(l + 1);
                for (int j = 0; j < col; j++) {
                    result[i][j] += colVal * B[colNum][j];
                }
            }
        }
        return result;
    }
}
```
``` java
public class Solution {
    public int[][] multiply(int[][] A, int[][] B) {
        int row1 = A.length, col1 = A[0].length, row2 = B.length, col2 = B[0].length;
        int[][] result = new int[row1][col2];
        
        for (int i = 0; i < row1; i++) {
            for (int j = 0; j < col2; j++) {
                for (int k = 0; k < col1; k++) {
                    result[i][j] += A[i][k] * B[k][j];
                }
            }
        }
        return result;
    }
}
```
