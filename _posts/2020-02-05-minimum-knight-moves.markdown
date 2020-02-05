---
layout: post
title: 1197 - Minimum Knight Moves
date: 2020-02-05
tags:
- Leetcode
categories:
- Matrix
author: Jason
---
In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0]. A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

```python
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        queue = [[0, 0, 0]]
        visited = {(0, 0)}
        x, y = abs(x), abs(y)
        while queue:
            x1, y1, step = queue.pop(0)
            if x1 == x and y1 == y:
                return step
            for x2, y2 in self.helper(x1, y1):
                if (x2, y2) not in visited and x2 > -2 and y2 > -2:
                    visited.add((x2, y2))
                    queue.append([x2, y2, step + 1])
        return -1

    def helper(self, i, j):
        return [(i - 2, j - 1), (i - 2, j + 1), (i + 2, j - 1), (i + 2, j + 1), (i - 1, j - 2), (i + 1, j - 2), (i - 1, j + 2), (i + 1, j + 2)]
```
