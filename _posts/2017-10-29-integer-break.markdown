---
layout: post
title: 343 - Integer Break
date: 2017-10-29
tags:
- Leetcode
categories:
- Dynamic Programming
author: Jason
---
**Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.**
* no cut on the left part, optimal cut on the right part;
* optimal cut on the left part, no cut on the right part;
* optimal cut on the left part, optimal cut on the right part;
* no cut on the left part, no cut on the right part;

```python
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 0
        dp = [1] * (n + 1)
        for i in xrange(2, n + 1):
            for j in xrange(1, i):
                dp[i] = max(dp[i], max(dp[j], j) * max(dp[i - j], i - j))
        return dp[-1]
```
