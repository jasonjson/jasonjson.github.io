---
layout: post
title: 367 - Valid Perfect Square
date: 2017-11-07
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Given a positive integer num, write a function which returns True if num is a perfect square else False.**


```python
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        lo, hi = 1, num
        while lo <= hi:
            mid = (lo + hi) / 2
            val = mid * mid
            if val == num:
                return True
            elif val < num:
                lo = mid + 1
            else:
                hi = mid - 1
        return False
```
