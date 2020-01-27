---
layout: post
title: 1031 - Maximum Sum Of Two Non-Overlapping Subarrays
date: 2020-01-26
tags:
- Leetcode
categories:
- Array
author: Jason
---
Given an array A of non-negative integers, return the maximum sum of elements in two non-overlapping (contiguous) subarrays, which have lengths L and M. (For clarification, the L-length subarray could occur before or after the M-length subarray.)

```python
class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        if not A:
            return 0

        for i in range(1, len(A)):
            A[i] += A[i - 1]

        L_max, M_max = A[L - 1], A[M - 1]
        ret = A[L + M - 1]
        for i in range(L + M, len(A)):
            L_max = max(L_max, A[i - M] - A[i - M - L])
            M_max = max(M_max, A[i - L] - A[i - M - L])
            ret = max(ret, L_max + A[i] - A[i - M], M_max + A[i] - A[i - L])
        return ret
```
