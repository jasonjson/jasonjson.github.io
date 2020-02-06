---
layout: post
title: 844 - Backspace String Compare
date: 2020-02-06
tags:
- Leetcode
categories:
- String
author: Jason
---
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

```python
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i, j = len(S) - 1, len(T) - 1
        back_s = back_t = 0
        while True:
            while i >= 0 and (back_s or S[i] == "#"):
                back_s += 1 if S[i] == "#" else -1
                i -= 1
            while j >= 0 and (back_t or T[j] == "#"):
                back_t += 1 if T[j] == "#" else -1
                j -= 1
            if i < 0 or j < 0 or S[i] != T[j]:
                return i == j == -1
            i -= 1
            j -= 1
        return True
```
