---
layout: post
title: 801 - Minimum Swaps To Make Sequence Increasing
date: 2020-02-03
tags:
- Leetcode
categories:
- Dynamic Programming
author: Jason
---
We have two integer sequences A and B of the same non-zero length. We are allowed to swap elements A[i] and B[i].  Note that both elements are in the same index position in their respective sequences. At the end of some number of swaps, A and B are both strictly increasing.  (A sequence is strictly increasing if and only if A[0] < A[1] < A[2] < ... < A[A.length - 1].) Given A and B, return the minimum number of swaps to make both sequences strictly increasing.  It is guaranteed that the given input always makes it possible.

```python
class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        swap, no_swap = [n] * n, [n] * n
        swap[0], no_swap[0] = 1, 0

        for i in range(1, n):
            if A[i - 1] < A[i] and B[i - 1] < B[i]:
                no_swap[i] = no_swap[i - 1]
                swap[i] = swap[i - 1] + 1
            if A[i - 1] < B[i] and B[i - 1] < A[i]:
                no_swap[i] = min(no_swap[i], swap[i - 1])
                swap[i] = min(swap[i], no_swap[i - 1] + 1)
        return min(swap[-1], no_swap[-1])
```
