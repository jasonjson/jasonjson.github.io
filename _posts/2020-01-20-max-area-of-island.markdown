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
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water. Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

```python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j]:
                grid[i][j] = 0
                return 1 + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)
            return 0

        areas = [dfs(i, j) for i in range(len(grid)) for j in range(len(grid[0]))]
        return max(areas) if areas else 0
```
