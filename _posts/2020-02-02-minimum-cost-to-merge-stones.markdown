---
layout: post
title: 1000 - Minimum Cost To Merge Stones
date: 2020-02-02
tags:
- Leetcode
categories:
- DP
author: Jason
---
There are N piles of stones arranged in a row.  The i-th pile has stones[i] stones. A move consists of merging exactly K consecutive piles into one pile, and the cost of this move is equal to the total number of stones in these K piles. Find the minimum cost to merge all piles of stones into one pile.  If it is impossible, return -1.

```python
from functools import lru_cache
class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        @lru_cache(None)
        def helper(i, j, m):
            if i == j:
                return 0 if m == 1 else float("inf")
            elif m == 1:
                return helper(i, j, K) + sum(stones[i: j + 1])
            else:
                return min(helper(i, mid, 1) + helper(mid + 1, j, m - 1) for mid in range(i, j))

        ret = helper(0, len(stones) - 1, 1)
        return ret if ret != float("inf") else -1
```
