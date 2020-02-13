---
layout: post
title: 787 - Cheapest Flights Within K Stops
date: 2020-01-30
tags:
- Leetcode
categories:
- Array
author: Jason
---
There are n cities connected by m flights. Each fight starts from city u and arrives at v with a price w. Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

```python
from heapq import heappush, heappop
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        price_map = defaultdict(list)
        for u, v, w in flights:
            price_map[u].append([v, w])

        heap = [[0, src, K + 1]]
        while heap:
            price, curr, stop = heappop(heap)
            if curr == dst:
                return price
            if stop > 0:
                for city, p in price_map[curr]:
                    heappush(heap, [price + p, city, stop - 1])
        return -1
```
