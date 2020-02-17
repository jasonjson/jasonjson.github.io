---
layout: post
title: 131 - Palindrome Partitioning
date: 2015-10-21 03:25:53.000000000 -04:00
tags:
- Leetcode
categories:
- DFS
author: Jason
---
**Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.**

``` python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []

        ret = []
        self.helper(s, [], ret)
        return ret

    def helper(self, s, curr, ret):
        if not s:
            ret.append(curr.copy())
            return
        for i in range(1, len(s) + 1):
            if self.is_pali(s[:i]):
                curr.append(s[:i])
                self.helper(s[i:], curr, ret)
                curr.pop()

    def is_pali(self, s):
        return s == s[::-1]
```
