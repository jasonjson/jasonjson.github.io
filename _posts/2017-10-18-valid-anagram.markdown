---
layout: post
title: 242 - Valid Anagram
date: 2017-10-18
tags:
- Leetcode
categories:
- String
author: Jason
---
**Given two strings s and t, write a function to determine if t is an anagram of s.**


```python
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        return sorted(s) == sorted(t)
```
