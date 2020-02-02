---
layout: post
title: 1152 - Analyze User Website Visit Pattern
date: 2020-02-01
tags:
- Leetcode
categories:
- Array
author: Jason
---
We are given some website visits: the user with name username[i] visited the website website[i] at time timestamp[i]. A 3-sequence is a list of websites of length 3 sorted in ascending order by the time of their visits.  (The websites in a 3-sequence are not necessarily distinct.) Find the 3-sequence visited by the largest number of users. If there is more than one solution, return the lexicographically smallest such 3-sequence.

```python
from collections import defaultdict, Counter
from itertools import combinations

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        user_sites_map = defaultdict(list)
        for _, u, w in sorted(zip(timestamp, username, website)):
            user_sites_map[u].append(w)

        counter = sum([Counter(set(combinations(v, 3))) for v in user_sites_map.values()], Counter())
        return list(min(counter, key=lambda x: (-counter[x], x)))
```
