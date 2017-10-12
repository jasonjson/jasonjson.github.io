---
layout: post
title: 202 - Happy Number
date: 2015-11-04 15:15:26.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Write an algorithm to determine if a number is "happy". A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.**

``` python
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum([int(c) ** 2 for c in str(n)])
        return n == 1
```
