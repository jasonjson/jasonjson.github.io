---
layout: post
title: 191 - Number Of 1 Bits
date: 2017-10-10
tags:
- Leetcode
categories:
- Bit
author: Jason
---
**Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).**


```python
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        ret = 0
        for i in xrange(32):
            if (n >> i) & 1:
                ret += 1
        return ret
```
