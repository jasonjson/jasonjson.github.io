---
layout: post
title: 317 - Shortest Distance from All Buildings
date: 2015-12-16 22:42:54.000000000 -05:00
tags:
- Leetcode
categories:
- Matrix
author: Jason
---
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You are given a 2D grid of values 0, 1 or 2. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

* Each 0 marks an empty land which you can pass by freely.
* Each 1 marks a building which you cannot pass through.
* Each 2 marks an obstacle which you cannot pass through.

``` python
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        row, col = len(grid), len(grid[0])
        dist_dict = [[0] * col for _ in range(row)]
        count_dict = [[0] * col for _ in range(row)]
        buildings = 0

        def bfs(queue, visited):
            while queue:
                i, j, distance = queue.pop(0)
                dist_dict[i][j] += distance
                count_dict[i][j] += 1
                for new_i, new_j in (i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1):
                    if 0 <= new_i < row and 0 <= new_j < col and grid[new_i][new_j] == 0 and not visited[new_i][new_j]:
                        visited[new_i][new_j] = True
                        queue.append([new_i, new_j, distance + 1])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    buildings += 1
                    visited = [[False] * col for _ in range(row)]
                    dfs([[i, j, 0]], visited)

        candidates = [dist_dict[i][j] for i in range(row) for j in range(col) if grid[i][j] == 0 and count_dict[i][j] == buildings]
        return min(candidates) if candidates else -1
```
