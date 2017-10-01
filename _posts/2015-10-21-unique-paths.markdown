---
layout: post
title: Unique Paths
date: 2015-10-21 12:25:13.000000000 -04:00
tags:
- Leetcode
categories:
- Dynamic Programming
author: Jason
---
**A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below). The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below). How many possible unique paths are there?**


``` java
public class Solution {
    /**
     * @param n, m: positive integer (1 <= n ,m <= 100)
     * @return an integer
     */
    public int uniquePaths(int m, int n) {
        if (m == 0 || n == 0) return 0;

        int[][] dp = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 || j == 0) {
                    dp[i][j] = 1; //这不是初始化,只是需要单独处理边界问题
                } else {
                    dp[i][j] = dp[i-1][j] + dp[i][j-1];
                }
            }
        }
        return dp[m-1][n-1];
    }
}
```

``` python
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        dp = [[0] * n for i in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        return dp[-1][-1]
```
