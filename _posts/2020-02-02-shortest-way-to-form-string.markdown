---
layout: post
title: 1055 - Shortest Way To Form String
date: 2020-02-02
tags:
- Leetcode
categories:
- String
author: Jason
---
From any string, we can form a subsequence of that string by deleting some number of characters (possibly no deletions). Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If the task is impossible, return -1.

```python
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        ret = j = 0

        while j < len(target):
            i = 0
            found = False
            while i < len(source) and j < len(target):
                if source[i] == target[j]:
                    j += 1
                    found = True
                i += 1
            if found:
                ret += 1
            else:
                return -1
        return ret
```
