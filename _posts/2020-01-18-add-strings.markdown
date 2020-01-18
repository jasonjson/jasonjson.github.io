---
layout: post
title: 415 - Add Strings
date: 2020-01-18
tags:
- Leetcode
categories:
- String
author: Jason
---
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

```python
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if not num1 or not num2:
            return ""

        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        ret = []
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(num1[i])
                i -= 1
            if j >= 0:
                carry += int(num2[j])
                j -= 1

            ret.append(str(carry % 10))
            carry //= 10

        return "".join(reversed(ret))
```
