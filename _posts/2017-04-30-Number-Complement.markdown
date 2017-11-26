---
layout: post
title: 476 - Number Complement
date: 2017-04-30
tags:
- Leetcode
categories:
- Bit
author: Jason
---
**Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.**


```python
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i = 1
        while i <= num:
            i = i << 1
        #eg: i = "10000", i - 1 = "1111"
        return (i - 1) ^ num
```
