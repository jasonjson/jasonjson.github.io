---
layout: post
title: 5 - Longest Palindromic Substring
date: 2015-10-21 02:14:16.000000000 -04:00
tags:
- Leetcode
categories:
- String
author: Jason
---
**Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.**

``` python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        ret = [0, 0] #start index, end index
        def helper(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > ret[1] - ret[0] + 1:
                ret[0] = left + 1
                ret[1] = right - 1

        for i in range(len(s)):
            helper(i, i)
            helper(i, i + 1)
        return s[ret[0]: ret[1] + 1]
```
