---
layout: post
title: 743 - Network Delay Time
date: 2020-02-04
tags:
- Leetcode
categories:
- Graph
author: Jason
---
There are N network nodes, labelled 1 to N. Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target. Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

```python
from collections import defaultdict
from heapq import heappush, heappop
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        neighbors = defaultdict(list)
        signal = {}
        pq = [(0, K)]
        for u, v, w in times:
            neighbors[u].append([v, w])
        while pq:
            time, node = heappop(pq)
            if node not in signal:
                signal[node] = time
                for v, w in neighbors[node]:
                    heappush(pq, (time + w, v))
        return max(signal.values()) if len(signal) == N else -1
```
