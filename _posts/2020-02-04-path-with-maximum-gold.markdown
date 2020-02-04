---
layout: post
title: 1219 - Path With Maximum Gold
date: 2020-02-04
tags:
- Leetcode
categories:
- Matrix
author: Jason
---
In a gold mine grid of size m * n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty. Return the maximum amount of gold you can collect under the conditions:

* Every time you are located in a cell you will collect all the gold in that cell.
* From your position you can walk one step to the left, right, up or down.
* You can't visit the same cell more than once.
* Never visit a cell with 0 gold.
* You can start and stop collecting gold from any position in the grid that has some gold.

```python
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    ret = max(ret, self.dfs(i, j, grid) + grid[i][j])
        return ret

    def dfs(self, i, j, grid):
        gold = 0
        grid[i][j], tmp = 0, grid[i][j]
        for new_i, new_j in (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j):
            if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]) and grid[new_i][new_j] != 0:
                gold = max(gold, self.dfs(new_i, new_j, grid) + grid[new_i][new_j])
        grid[i][j] = tmp
        return gold
```
