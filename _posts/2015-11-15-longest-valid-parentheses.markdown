---
layout: post
title: 32 - Longest Valid Parentheses
date: 2015-11-15 10:28:38.000000000 -05:00
tags:
- Leetcode
categories:
- String
author: Jason
---
**Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.**

``` python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ret = 0
        stack = []
        dp = [0] * (len(s) + 1)
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif stack:
                p = stack.pop()
                dp[i + 1] = dp[p] + i - p + 1
        return max(dp)
```
