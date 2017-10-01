---
layout: post
title: Matrix Zigzag Traversal
date: 2015-10-21 13:04:40.000000000 -04:00
tags:
- Leetcode
categories:
- Matrix
author: Jason
---
<p><strong><em>Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in ZigZag-order.</em></strong></p>


``` java
public class Solution {
    /**
     * @param matrix: a matrix of integers
     * @return: an array of integers
     */ 
    //http://algorithm.yuanbin.me/zh-cn/problem_misc/matrix_zigzag_traversal.html
    public int[] printZMatrix(int[][] matrix) {
        if (matrix == null || matrix.length == 0) return null;
        
        int m = matrix.length; int n = matrix[0].length;
        int[] result = new int[m * n];
        int index = 0;
        for (int i = 0; i < m + n; i++) {
            if (i % 2 == 0) {
                for (int x = i; x >= 0; x --) {
                    if (x < m && i - x < n) {
                        result[index++] = matrix[x][i-x];
                    }
                }
            } else {
                for (int x = 0; x <= i; x ++) {
                    if (x < m && i - x < n) {
                        result[index++] = matrix[x][i-x];
                    }
                }
            }
        }
        return result;
    }
}
```
