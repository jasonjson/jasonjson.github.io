---
layout: post
title: 139 - Word Break
date: 2015-10-21 12:34:38.000000000 -04:00
tags:
- Leetcode
categories:
- Dynamic Programming
author: Jason
---
**Given a string s and a dictionary of words dict, determine if s can be break into a space-separated sequence of one or more dictionary words.**

``` python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not wordDict:
            return False

        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j: i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]
```
