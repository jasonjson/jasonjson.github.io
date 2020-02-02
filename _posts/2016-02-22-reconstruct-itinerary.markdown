---
layout: post
title: 332 - Reconstruct Itinerary
date: 2016-02-22 22:26:53.000000000 -05:00
tags:
- Leetcode
categories:
- DFS Backtracking
author: Jason
---
**Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.**

``` python
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        if not tickets:
            return []

        iter_map = defaultdict(list)
        for a, b in tickets:
            iter_map[a].append(b)
        [v.sort() for _, v in iter_map.items()]
        ret = ["JFK"]
        self.helper(iter_map, ret, len(tickets) + 1)
        return ret

    def helper(self, iter_map, ret, total_stops):
        if len(ret) == total_stops:
            return True

        next_stops = iter_map[ret[-1]]
        for i in range(len(next_stops)):
            ret.append(next_stops.pop(i))
            if self.helper(iter_map, ret, total_stops):
                return True
            next_stops.insert(i, ret.pop())
        return False
```
