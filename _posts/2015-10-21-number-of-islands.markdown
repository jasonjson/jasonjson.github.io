---
layout: post
title: 200 - Number of Islands
date: 2015-10-21 03:02:22.000000000 -04:00
tags:
- Leetcode
categories:
- Matrix
author: Jason
---
**Given a boolean 2D matrix, find the number of islands.**


``` java
public class Solution {
    public int numIslands(boolean[][] grid) {
        if (grid == null || grid.length == 0) return 0;
        int row = grid.length, col = grid[0].length;

        int count = 0;
        for (int i = 0; i < row; i ++) {
            for (int j = 0; j < col; j++) {
                if (grid[i][j]) {
                    count ++;
                    dfs(grid, i, j);
                }
            }
        }
        return count;
    }

    public void dfs(boolean[][] grid, int i, int j) {
        if (i < 0 || i >= grid.length || j < 0 || j >= grid[0].length || !grid[i][j]) return;
        grid[i][j] = false;
        dfs(grid, i - 1, j);
        dfs(grid, i + 1, j);
        dfs(grid, i, j - 1);
        dfs(grid, i, j + 1);
    }
}
```

``` python
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        row, col = len(grid), len(grid[0])
        ret = 0
        for i in xrange(row):
            for j in xrange(col):
                if grid[i][j] == "1":
                    self.helper(grid, i, j)
                    ret += 1
        return ret

    def helper(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != "1" or not grid[i][j]:
            return
        grid[i][j] = False
        self.helper(grid, i - 1, j)
        self.helper(grid, i + 1, j)
        self.helper(grid, i, j - 1)
        self.helper(grid, i, j + 1)
```
