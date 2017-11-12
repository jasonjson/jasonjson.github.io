---
layout: post
title: 399 - Evaluate Division
date: 2017-11-12
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.**


```python
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """

        division_map = collections.defaultdict(dict)
        for (a, b), v in zip(equations, values):
            division_map[a][a] = 1.0
            division_map[b][b] = 1.0
            division_map[a][b] = v
            division_map[b][a] = 1.0 / v

        for k in division_map:
            for i in division_map[k]:
                for j in division_map[k]:
                    division_map[i][j] = division_map[i][k] * division_map[k][j]

        return [division_map[a].get(b, -1.0) for a, b in queries]
```
