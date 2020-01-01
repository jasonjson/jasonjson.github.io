---
layout: post
title: 221 - Maximal Square
date: 2015-11-03 15:29:44.000000000 -05:00
tags:
- Leetcode
categories:
- Dynamic Programming
author: Jason
---
**Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.**


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

``` python
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        ret = 0
        dp = [[int(matrix[i][j]) for j in range(len(matrix[0]))] for i in range(len(matrix))]
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
        ret = max([max(row) for row in dp])
        return ret ** 2
```
