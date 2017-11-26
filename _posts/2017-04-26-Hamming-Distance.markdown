---
layout: post
title: 461 - Hamming Distance
date: 2017-04-26
tags:
- Leetcode
categories:
- Bit
author: Jason
---
**The Hamming distance between two integers is the number of positions at which the corresponding bits are different. Given two integers x and y, calculate the Hamming distance.**


```python
class Solution(object):
    def hammingDistance(self, x, y):
        xor = x ^ y
        count = 0
        for _ in xrange(32):
            if xor & 1 == 1:
                count += 1
            xor >>= 1
        return count
```
