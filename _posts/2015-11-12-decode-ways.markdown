---
layout: post
title: 91 - Decode Ways
date: 2015-11-12 12:13:00.000000000 -05:00
tags:
- Leetcode
categories:
- Dynamic Programming
author: Jason
---
**A message containing letters from A-Z is being encoded to numbers using the following mapping:**

* A -> 1
* B -> 2
* ...
* Z -> 26

**Given an encoded message containing digits, determine the total number of ways to decode it.**

``` python
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        dp = [0] * (len(s) + 1)
        dp[0] = dp[1] = 1
        for i in range(2, len(s) + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            if 10 <= int(s[i-2: i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]
```
