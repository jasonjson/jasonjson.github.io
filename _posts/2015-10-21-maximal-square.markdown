---
layout: post
title: Maximal Square
date: 2015-10-21 14:29:56.000000000 -04:00
tags: algorithm
categories:
- Dynamic Programming
- Matrix
author: Jason
---
<p><strong><em>Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.</em></strong></p>


``` java
public class Solution {
    /**
     * @param matrix: a matrix of 0 and 1
     * @return: an integer
     */
    public int maxSquare(int[][] matrix) {
        // write your code here
        if (matrix == null || matrix.length == 0) return 0;
        int row = matrix.length, col = matrix[0].length;
        
        int[][] dp = new int[row][col];
        int max = 0;
        for (int i = 0; i < row; i++) {
            if (matrix[i][0] == 1) {
                dp[i][0] = 1;
                max = 1;
            }
        }
        
        for (int j = 0; j < col; j++) {
            if (matrix[0][j] == 1) {
                dp[0][j] = 1;
                max = 1;
            }
        }
        
        for (int i = 1; i < row; i++) {
            for (int j = 1; j < col; j++) {
                if (matrix[i][j] == 1) {
                    dp[i][j] = Math.min(dp[i-1][j], Math.min(dp[i][j-1], dp[i-1][j-1])) + 1;
                    max = Math.max(max, dp[i][j]);
                }
            }
        }
        return max * max;
    }
}//http://www.cnblogs.com/jcliBlogger/p/4548751.html
```
