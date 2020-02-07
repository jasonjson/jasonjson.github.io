---
layout: post
title: 896 - Monotonic Array
date: 2020-02-07
tags:
- Leetcode
categories:
- Array
author: Jason
---
An array is monotonic if it is either monotone increasing or monotone decreasing. An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j]. Return true if and only if the given array A is monotonic.

```python
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if not A:
            return True

        increase = decrease = False
        for i in range(1, len(A)):
            if A[i] < A[i - 1]:
                decrease = True
            elif A[i] > A[i - 1]:
                increase = True
        return False if decrease and increase else True
```
