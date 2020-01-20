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
from heapq import heapify, heappush, heappop
from collections import Counter
class Solution:
    def reorganizeString(self, S: str) -> str:
        if not S:
            return ""

        pq = [(-v, k) for k, v in Counter(S).items()]
        heapify(pq)
        ret = []
        prev_count, prev_c = 0, ""
        while pq:
            count, c = heappop(pq)
            ret.append(c)
            count += 1
            if prev_count < 0:
                heappush(pq, (prev_count, prev_c))
            prev_count, prev_c = count, c
        return "".join(ret) if len(ret) == len(S) else ""
```
