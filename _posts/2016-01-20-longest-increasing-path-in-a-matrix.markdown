---
layout: post
title: Longest Increasing Path in a Matrix
date: 2016-01-20 11:57:16.000000000 -05:00
tags:
- Leetcode
categories:
- DFS Backtracking
author: Jason
---
<p><strong><em>Given an integer matrix, find the length of the longest increasing path. From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).</em></strong></p>


``` java
public class Solution {
    public static int longestIncreasingPath(int[][] matrix) {
        if (matrix == null || matrix.length == 0) return 0;

        int row = matrix.length, col = matrix[0].length, result = 0;
        int[][] dp = new int[row][col];
        for (int i = 0; i < row; i++) {
            Arrays.fill(dp[i], 1);
        }
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                result = Math.max(result, helper(matrix, dp, i, j));
            }
        }
        return result;
    }

    public static int helper(int[][] matrix, int[][] dp, int i, int j) {
        if (i < 0 || i >= matrix.length || j < 0 || j >= matrix[0].length) return 0;
        if (dp[i][j] != 1) return dp[i][j];
        if (i - 1 >= 0 && matrix[i][j] > matrix[i - 1][j]) {
            dp[i][j] = Math.max(dp[i][j], helper(matrix, dp, i - 1, j) + 1);
        }
        if (i + 1 < matrix.length && matrix[i][j] > matrix[i + 1][j]) {
            dp[i][j] = Math.max(dp[i][j], helper(matrix, dp, i + 1, j) + 1);
        }
        if (j - 1 >= 0 && matrix[i][j] > matrix[i][j - 1]) {
            dp[i][j] = Math.max(dp[i][j], helper(matrix, dp, i, j - 1) + 1);
        }
        if (j + 1 < matrix[0].length && matrix[i][j] > matrix[i][j + 1]) {
            dp[i][j] = Math.max(dp[i][j], helper(matrix, dp, i, j + 1) + 1);
        }
        return dp[i][j];
    }
}
```
