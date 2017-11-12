---
layout: post
title: 396 - Rotate Function
date: 2017-11-12
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Given an array of integers A and let n to be its length. Assume Bk to be an array obtained by rotating the array A k positions clock-wise, we define a "rotation function" F on A as follow: F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1]. Calculate the maximum value of F(0), F(1), ..., F(n-1).**


```python
class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        #F[k] = F[k-1] + summation - nBk[0]
        if not A:
            return 0
        summation = sum(A)
        ret = F = sum([i * num for i, num in enumerate(A)])
        for i in xrange(1, len(A)):
            F = F + summation - len(A) * A[-i]
            ret = max(ret, F)
        return ret
```
