---
layout: post
title: 1192 - Critical Connections In A Network
date: 2020-02-09
tags:
- Leetcode
categories:
- DFS Backtracking
author: Jason
---
from typing import List
from collections import defaultdict
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        conn_dict = defaultdict(list)
        for a, b in connections:
            conn_dict[a].append(b)
            conn_dict[b].append(a)
        visited = [False] * n

        ret = []
        rank = list(range(n))
        def dfs(curr, prev, curr_rank):
            rank[curr] = curr_rank
            visited[curr] = True
            for neighbor in conn_dict[curr]:
                if neighbor == prev:
                    continue
                if not visited[neighbor]:
                    dfs(neighbor, curr, curr_rank + 1)
                rank[curr] = min(rank[curr], rank[neighbor])
                if curr_rank < rank[neighbor]:
                    ret.append([curr, neighbor])
        dfs(0, -1, 0)
        return ret

```python
from collections import defaultdict
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        conn_dict = defaultdict(list)
        for a, b in connections:
            conn_dict[a].append(b)
            conn_dict[b].append(a)
        visited = [False] * n

        ret = []
        rank = list(range(n))
        def dfs(curr, prev, curr_rank):
            rank[curr] = curr_rank
            visited[curr] = True
            for neighbor in conn_dict[curr]:
                if neighbor == prev:
                    continue
                if not visited[neighbor]:
                    dfs(neighbor, curr, curr_rank + 1)
                rank[curr] = min(rank[curr], rank[neighbor])
                if curr_rank < rank[neighbor]:
                    ret.append([curr, neighbor])
        dfs(0, -1, 0)
        return ret
```
