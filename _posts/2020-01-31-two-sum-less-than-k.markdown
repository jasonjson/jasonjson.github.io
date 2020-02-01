---
layout: post
title: 1099 - Two Sum Less Than K
date: 2020-01-31
tags:
- Leetcode
categories:
- Array
author: Jason
---
Given an array A of integers and integer K, return the maximum S such that there exists i < j with A[i] + A[j] = S and S < K. If no i, j exist satisfying this equation, return -1.

```python
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        if not A:
            return -1

        A.sort()
        lo, hi = 0, len(A) - 1
        ret = -float("inf")
        while lo < hi:
            S = A[lo] + A[hi]
            if S < K:
                ret = max(ret, S)
                lo += 1
            else:
                hi -= 1
        return ret if ret != -float("inf") else -1
```
