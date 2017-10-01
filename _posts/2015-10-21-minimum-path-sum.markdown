---
layout: post
title: 64 - Minimum Path Sum
date: 2015-10-21 12:24:23.000000000 -04:00
tags:
- Leetcode
categories:
- Dynamic Programming
author: Jason
---
**Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.**


``` java
public class Solution {
    /**
     * @param grid: a list of lists of integers.
     * @return: An integer, minimizes the sum of all numbers along its path
     */
    public int minPathSum(int[][] grid) {
        // write your code here
        int row = grid.length, col = grid[0].length;
        if (grid == null || row == 0 || col == 0) return 0;

        for (int i = 0; i < row; i ++) {
            for (int j = 0; j < col; j ++) {
                if (i == 0 && j == 0) continue;
                else if (i == 0) {
                    grid[i][j] += grid[i][j-1];
                } else if (j == 0) {
                    grid[i][j] += grid[i-1][j];
                } else {
                    grid[i][j] += Math.min(grid[i-1][j], grid[i][j-1]);
                }
            }
        }

        //after this, grid[i][j] denotes the smallest sum from [0][0] to [i][j],
        //since each time we find the smallest sum so far and add it to the current value at original grid[i][j]
        // 1 3 1     1 4 5
        // 1 5 1  => 2 7 6
        // 4 2 1     6 8 7
        return grid[row-1][col-1];
    }
}
```
``` java
public class Solution {
    /**
     * @param grid: a list of lists of integers.
     * @return: An integer, minimizes the sum of all numbers along its path
     */
    public int minPathSum(int[][] grid) {
        if (grid == null || grid.length == 0) return 0;

        int row = grid.length, col = grid[0].length;
        int[][] path = new int[row][col];
        for (int i = 0; i < row; i++) {
            if (i == 0) {
                path[i][0] = grid[i][0];
            } else {
                path[i][0] = grid[i][0] + path[i-1][0];
            }
        }
        for (int j = 1; j < col; j++) {
            path[0][j] += grid[0][j] + path[0][j-1];
        }

        for (int i = 1; i < row; i++) {
            for (int j = 1; j < col; j++) {
                path[i][j] = Math.min(path[i-1][j], path[i][j-1]) + grid[i][j];
            }
        }
        return path[row-1][col-1];
    }
}
```

``` python
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if not grid:
            return 0

        row, col = len(grid), len(grid[0])
        dp = [[0] * col for i in xrange(row)]

        dp[0][0] = grid[0][0]
        for i in xrange(1, row):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in xrange(1, col):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        dp[0][0] = grid[0][0]
        for i in xrange(1, row):
            for j in xrange(1, col):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]
```
