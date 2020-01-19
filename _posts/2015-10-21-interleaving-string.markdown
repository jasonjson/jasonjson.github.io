---
layout: post
title: 97 - Interleaving String
date: 2015-10-21 12:49:37.000000000 -04:00
tags:
- Leetcode
categories:
- Dynamic Programming
author: Jason
---
Given three strings: s1, s2, s3, determine whether s3 is formed by the interleaving of s1 and s2.

``` python
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s1 and not s2 and not s3:
            return True
        elif len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[0][0] = True
        for i in range(1, len(s1) + 1):
            if s1[i - 1] == s3[i - 1]:
                dp[i][0] = dp[i - 1][0]
        for j in range(1, len(s2) + 1):
            if s2[j - 1] == s3[j - 1]:
                dp[0][j] = dp[0][j - 1]

        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] |= dp[i - 1][j]
                if s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] |= dp[i][j - 1]
        return dp[-1][-1]
```
