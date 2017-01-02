---
layout: post
title: Number of Islands
date: 2015-10-21 03:02:22.000000000 -04:00
categories:
- DFS Backtracking
- Matrix
author: Jason
---
<p><strong><em>Given a boolean 2D matrix, find the number of islands.</em></strong><br />


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
