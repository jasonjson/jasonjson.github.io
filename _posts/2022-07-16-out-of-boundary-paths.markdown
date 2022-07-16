---
layout: post
title: 576 - Out Of Boundary Paths
date: 2022-07-16
tags:
- Leetcode
categories:
- DYNAMIC PROGRAMMING
author: Jason
---
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.

```python
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = {}
        def helper(maxMove, i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            elif maxMove == 0:
                return 0
            elif (maxMove, i, j) not in dp:
                a = helper(maxMove - 1, i - 1, j)
                b = helper(maxMove - 1, i + 1, j)
                c = helper(maxMove - 1, i, j - 1)
                d = helper(maxMove - 1, i, j + 1)
                dp[(maxMove, i, j)] = (a + b + c + d) % 1000000007
            return dp[(maxMove, i, j)]
        return helper(maxMove, startRow, startColumn)
```
