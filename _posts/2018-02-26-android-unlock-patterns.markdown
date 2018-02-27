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
class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        dist_map = {"13":2, "17":4, "39": 6, "79":8, "19": 5, "37": 5, "28": 5, "46" :5}
        visited = [False] * 10
        ret = 0
        for remain in xrange(m, n + 1):
            ret += self.helper(1, dist_map, visited, remain - 1) * 4
            ret += self.helper(2, dist_map, visited, remain - 1) * 4
            ret += self.helper(5, dist_map, visited, remain - 1)
        return ret

    def helper(self, curr, dist_map, visited, remain):
        if remain == 0:
            return 1
        visited[curr] = True
        ret = 0
        for i in xrange(1, 10):
            cross = dist_map.get(str(i) + str(curr), 0) or dist_map.get(str(curr) + str(i), 0)
            if not visited[i] and (cross == 0 or visited[cross]):
                ret += self.helper(i, dist_map, visited, remain - 1)
        visited[curr] = False
        return ret
```
