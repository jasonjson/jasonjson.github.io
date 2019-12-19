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
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    ret += 1
                    self.helper(grid, i, j)
        return ret

    def helper(self, grid, i, j):
        grid[i][j] = "2"
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for dx, dy in directions:
            new_i, new_j = i + dx, j + dy
            if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]) and grid[new_i][new_j] == "1":
                self.helper(grid, new_i, new_j)
```
