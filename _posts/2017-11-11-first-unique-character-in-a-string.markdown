---
layout: post
title: 387 - First Unique Character In A String
date: 2017-11-11
tags:
- Leetcode
categories:
- String
author: Jason
---
**Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.**


```python
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        if not s:
            return -1
        counter = collections.Counter(s)
        for i, char in enumerate(s):
            if counter.get(char) == 1:
                return i
        return -1
```
