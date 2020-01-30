---
layout: post
title: 1057 - Campus Bikes
date: 2020-01-29
tags:
- Leetcode
categories:
- Array
author: Jason
---
On a campus represented as a 2D grid, there are N workers and M bikes, with N <= M. Each worker and bike is a 2D coordinate on this grid. Our goal is to assign a bike to each worker. Among the available bikes and workers, we choose the (worker, bike) pair with the shortest Manhattan distance between each other, and assign the bike to that worker. (If there are multiple (worker, bike) pairs with the same shortest Manhattan distance, we choose the pair with the smallest worker index; if there are multiple ways to do that, we choose the pair with the smallest bike index). We repeat this process until there are no available workers. Return a vector ans of length N, where ans[i] is the index (0-indexed) of the bike that the i-th worker is assigned to.

```python
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        distance = []
        for i, (x1, y1) in enumerate(workers):
            for j, (x2, y2) in enumerate(bikes):
                distance.append([abs(x1 - x2) + abs(y1 - y2), i, j])
        distance.sort()

        ret = [-1] * len(workers)
        used = set()
        for _, i, j in distance:
            if ret[i] == -1 and j not in used:
                ret[i] = j
                used.add(j)
        return ret
```
