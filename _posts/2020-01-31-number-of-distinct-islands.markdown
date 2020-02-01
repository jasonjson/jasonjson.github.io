---
layout: post
title: 694 - Number Of Distinct Islands
date: 2020-01-31
tags:
- Leetcode
categories:
- Matrix
author: Jason
---
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water. Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

```python
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        islands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    path = []
                    self.helper(grid, i, j, path, "o")
                    islands.add("".join(path))
        return len(islands)

    def helper(self, grid, i, j, path, direction):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
            path.append(direction)
            grid[i][j] = 0
            self.helper(grid, i - 1, j, path, "l")
            self.helper(grid, i + 1, j, path, "r")
            self.helper(grid, i, j - 1, path, "u")
            self.helper(grid, i, j + 1, path, "d")
            path.append("b")
```
