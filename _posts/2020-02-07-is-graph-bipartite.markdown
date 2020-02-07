---
layout: post
title: 785 - Is Graph Bipartite
date: 2020-02-07
tags:
- Leetcode
categories:
- Graph
author: Jason
---
Given an undirected graph, return true if and only if it is bipartite. Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B. The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

```python
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        #A: 0, B: 1, 1 - 0 -> 1, 1 - 1 -> 0
        color = {}
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor in color:
                    if color[neighbor] == color[node]:
                        return False
                else:
                    color[neighbor] = 1 - color[node]
                    if not dfs(neighbor):
                        return False
            return True

        for i in range(len(graph)):
            if i not in color:
                color[i] = 0
                if not dfs(i):
                    return False
        return True
```
