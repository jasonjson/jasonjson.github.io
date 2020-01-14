---
layout: post
title: 370 - Range Addition
date: 2018-02-27
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Assume you have an array of length n initialized with all 0's and are given k update operations. Each operation is represented as a triplet: [startIndex, endIndex, inc] which increments each element of subarray A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc. Return the modified array after all k operations were executed.**


```python
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:

        if not length:
            return []

        ret = [0] * length
        for (start, end, num) in updates:
            ret[start] += num
            if end + 1 < length:
                ret[end + 1] -= num

        summation = 0
        for i in xrange(length):
            summation += ret[i]
            ret[i] = summation
        return ret
```
