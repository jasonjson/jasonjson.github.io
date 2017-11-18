---
layout: post
title: 463 - Island Perimeter
date: 2017-05-03
tags:
- Leetcode
categories:
- Array
author: Jason
---
**You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.**

```python
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        return sum(self.get_water(i, j, grid) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j])

    def get_water(self, i, j, grid):
        num = 0
        if i - 1 >= 0 or grid[i - 1][j] == 0:
            num += 1
        if i == len(grid) - 1 or grid[i + 1][j] == 0:
            num += 1
        if j - 1 >= 0 or grid[i][j - 1] == 0:
            num += 1
        if j == len(grid[0]) - 1 or grid[i][j + 1] == 0:
            num += 1
        return num
```

``` python
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        return sum(self.count(grid, i, j) for i in xrange(len(grid)) for j in xrange(len(grid[0])))

    def count(self, grid, i, j):
        if grid[i][j] == 0:
            return 0
        num = 4
        if i - 1 >= 0 and grid[i - 1][j] == 1:
            num -= 1
        if i + 1 < len(grid) and grid[i + 1][j] == 1:
            num -= 1
        if j - 1 >= 0 and grid[i][j - 1] == 1:
            num -= 1
        if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
            num -= 1
        return num
```
