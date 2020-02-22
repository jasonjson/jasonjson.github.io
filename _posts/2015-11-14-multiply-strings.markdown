---
layout: post
title: 43 - Multiply Strings
date: 2015-11-14 21:01:30.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Given two numbers represented as strings, return multiplication of the numbers as a string.**

``` python
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ret = [0] * (len(num1) + len(num2))
        for i in reversed(range(len(num1))):
            for j in reversed(range(len(num2))):
                num = int(num1[i]) * int(num2[j]) + ret[i + j + 1]
                ret[i + j + 1] = num % 10
                ret[i + j] += num // 10

        start = 0
        while start < len(ret):
            if ret[start] != 0:
                break
            start += 1
        return "".join(map(str, ret[start:])) or "0"
```
