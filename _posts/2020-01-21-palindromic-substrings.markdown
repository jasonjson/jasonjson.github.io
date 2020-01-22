---
layout: post
title: 647 - Palindromic Substrings
date: 2020-01-21
tags:
- Leetcode
categories:
- String
author: Jason
---
Given a string, your task is to count how many palindromic substrings in this string. The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0

        def count(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        ret = 0
        for i in range(len(s)):
            ret += count(i, i)
            ret += count(i, i + 1)
        return ret
```
