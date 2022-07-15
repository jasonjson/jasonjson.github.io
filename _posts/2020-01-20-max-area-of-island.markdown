---
layout: post
title: 695 - Max Area Of Island
date: 2020-01-20
tags:
- Leetcode
categories:
- Array
author: Jason
---
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

```python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ret = max(ret, self.dfs(grid, i, j))
        return ret
    def dfs(self, grid, i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j]:
            grid[i][j] = 0
            return 1 + self.dfs(grid, i - 1, j) + self.dfs(grid, i + 1, j) + self.dfs(grid, i, j - 1) + self.dfs(grid, i, j + 1)
        return 0
```
