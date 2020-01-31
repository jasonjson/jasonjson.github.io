---
layout: post
title: 204 - Count Primes
date: 2015-11-04 14:55:54.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Count the number of prime numbers less than a non-negative number, n.**

``` python
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        dp = [True] * n
        dp[0] = dp[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if dp[i]:
                for j in range(i * i, n, i):
                    dp[j] = False
        return sum(dp)
```
