---
layout: post
title: 560 - Subarray Sum Equals K
date: 2019-12-20
tags:
- Leetcode
categories:
- Array
author: Jason
---
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

```python
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr = ret = 0
        sum_map = defaultdict(int)
        sum_map[0] = 1
        for i, num in enumerate(nums):
            curr += num
            ret += sum_map[curr - k]
            sum_map[curr] += 1
        return ret
```
