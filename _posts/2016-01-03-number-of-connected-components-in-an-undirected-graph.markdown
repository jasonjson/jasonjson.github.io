---
layout: post
title: 323 - Number of Connected Components in an Undirected Graph
date: 2016-01-03 19:50:36.000000000 -05:00
tags:
- Leetcode
categories:
- Graph
author: Jason
---
**Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.**

``` python
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        union = {}

        def find(node):
            if union.setdefault(node, node) == node:
                return node
            else:
                return find(union[node])

        for a, b in edges:
            p1 = find(a)
            p2 = find(b)
            union[p1] = p2

        return len({find(i) for i in range(n)})
```
