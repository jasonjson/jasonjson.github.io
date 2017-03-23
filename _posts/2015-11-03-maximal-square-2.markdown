---
layout: post
title: Maximal Square
date: 2015-11-03 15:29:44.000000000 -05:00
tags:
- Algorithm
categories:
- Dynamic Programming
author: Jason
---
<p><strong><em>Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.</em></strong></p>


``` java
public class Solution {
    public int maximalSquare(char[][] matrix) {
        if (matrix == null || matrix.length == 0) return 0;

        int row = matrix.length, col = matrix[0].length, max = 0;
        int[][] dp = new int[row][col];
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (i == 0 || j == 0) {
                    dp[i][j] = matrix[i][j] - '0';
                } else if (matrix[i][j] == '1') {
                    dp[i][j] = Math.min(dp[i-1][j], Math.min(dp[i][j-1], dp[i-1][j-1])) + 1;
                }
                max = Math.max(max, dp[i][j]);
            }
        }
        return max * max;
    }
}
```
