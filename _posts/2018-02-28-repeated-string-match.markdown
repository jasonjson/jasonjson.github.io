---
layout: post
title: 686 - Repeated String Match
date: 2018-02-28
tags:
- Leetcode
categories:
- String
author: Jason
---
**Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.**


```python
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """

        C = ""
        for i in range(len(B)/len(A) + 3):
            if B in C:
                return i
            C += A
        return -1
```
