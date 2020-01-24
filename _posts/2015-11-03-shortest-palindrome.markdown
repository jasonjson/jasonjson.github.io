---
layout: post
title: 214 - Shortest Palindrome
date: 2015-11-03 17:45:22.000000000 -05:00
tags:
- Leetcode
categories:
- String
author: Jason
---
**Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.**

``` python
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s

        j = 0
        for i in reversed(range(len(s))):
            if s[i] == s[j]:
                j += 1
        return s[::-1][:len(s) - j] + self.shortestPalindrome(s[:j-len(s)]) + s[j-len(s):]
```
