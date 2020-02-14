---
layout: post
title: 278 - First Bad Version
date: 2015-10-21 02:28:07.000000000 -04:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**The code base version is an integer start from 1 to n. One day, someone committed a bad version in the code case, so it caused this version and the following versions are all failed in the unit tests. Find the first bad version.**


``` python
class Solution:
    def firstBadVersion(self, n: int):

        lo, hi = 1, n
        while lo <= hi:
            mid = (lo + hi) // 2
            if isBadVersion(mid):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo
```
