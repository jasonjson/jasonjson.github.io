---
layout: post
title: 351 - Android Unlock Patterns
date: 2018-02-26
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9, count the total number of unlock patterns of the Android lock screen, which consist of minimum of m keys and maximum n keys.**


```python
class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        cross_dict = {"13":2, "17": 4, "79": 8, "39": 6, "28": 5, "46":5, "19":5, "37": 5}
        visited = [False] * 10

        def helper(curr, remain):
            if remain == 0:
                return 1
            visited[curr] = True
            found = 0
            for i in range(1, 10):
                cross = cross_dict.get(str(i) + str(curr), 0) + cross_dict.get(str(curr) + str(i), 0)
                if not visited[i] and (cross == 0 or visited[cross]):
                    found += helper(i, remain - 1)
            visited[curr] = False
            return found

        ret = 0
        for i in range(m, n + 1):
            ret += helper(1, i - 1) * 4
            ret += helper(2, i - 1) * 4
            ret += helper(5, i - 1)
        return ret
```
