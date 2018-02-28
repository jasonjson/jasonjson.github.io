---
layout: post
title: 524 - Longest Word In Dictionary Through Deleting
date: 2018-02-28
tags:
- Leetcode
categories:
- String
author: Jason
---
**Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.**


```python
class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """

        if not d:
            return ""

        d.sort(key = lambda x : (-len(x), x))
        for candidate in d:
            j = 0
            for char in s:
                if j < len(candidate) and char == candidate[j]:
                    j += 1
            if j == len(candidate):
                return candidate
        return ""
```
