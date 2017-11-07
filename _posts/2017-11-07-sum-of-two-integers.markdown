---
layout: post
title: 371 - Sum Of Two Integers
date: 2017-11-07
tags:
- Leetcode
categories:
- Bit
author: Jason
---
**Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.**


```python
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX = 2 ** 31 - 1
        MIN = - 2 * 31
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # ^ get different bits and & gets double 1s, << moves carry
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~ (a ^ mask)
```
