---
layout: post
title: 395 - Longest Substring With At Least K Repeating Characters
date: 2017-11-12
tags:
- Leetcode
categories:
- String
author: Jason
---
**Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.**


```python
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        #If every character appears at least k times, the whole string is ok. Otherwise split by the first character appearing less than k times (because it will always be too infrequent and thus can't be part of any ok substring) and make the most out of the splits.

        for c in s:
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)
```
