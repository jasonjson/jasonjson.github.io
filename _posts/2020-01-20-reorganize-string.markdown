---
layout: post
title: 767 - Reorganize String
date: 2020-01-20
tags:
- Leetcode
categories:
- String
author: Jason
---
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same. If possible, output any possible result.  If not possible, return the empty string.

```python
from heapq import heappush, heappop
from collections import Counter
class Solution:
    def reorganizeString(self, S: str) -> str:
        if not S:
            return ""

        pq = sorted([-v, k] for k, v in Counter(S).items())
        ret = []
        prev_count, prev = 0, ""
        while pq:
            curr_count, curr = heappop(pq)
            ret.append(curr)
            curr_count += 1
            if prev_count < 0:
                heappush(pq, [prev_count, prev])
            prev_count, prev = curr_count, curr
        return "".join(ret) if len(ret) == len(S) else ""
```
