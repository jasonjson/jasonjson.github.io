---
layout: post
title: 342 - Power Of Four
date: 2017-11-06
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Given an integer (signed 32 bits), write a function to check whether it is a power of 4.**


```python
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """

        return num != 0 and num & (num - 1) == 0 and num & 1431655765 == num
```
