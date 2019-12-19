---
layout: post
title: 994 - Rotting Oranges
date: 2019-12-19
tags:
- Leetcode
categories: DFS
-
author: Jason
---
**In a given grid, each cell can have one of three values:**

* the value 0 representing an empty cell;
* the value 1 representing a fresh orange;
* the value 2 representing a rotten orange.
**Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten. Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.**

```python
from itertools import product
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        prev = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 2]
        ret = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while True:
            curr = []
            for (i, j), (dx, dy) in product(prev, directions):
                new_i, new_j = i + dx, j + dy
                if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]) and grid[new_i][new_j] == 1:
                    grid[new_i][new_j] = 2
                    curr.append((new_i, new_j))
            if not curr:
                break
            prev = curr
            ret += 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return ret
```
