---
layout: post
title: 357 - Count Numbers With Unique Digits
date: 2017-11-07
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.**


```python
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        ret = 10
        available_number = 9
        unique_digit = 9
        while n > 1:
            unique_digit *= available_number
            ret += unique_digit
            n -= 1
            available_number -= 1
        return ret
```
