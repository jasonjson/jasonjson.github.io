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
        prev_sum = ret = 0
        sum_map = defaultdict(int)
        for i, num in enumerate(nums):
            prev_sum += num
            if prev_sum == k:
                ret += 1
            if prev_sum - k in sum_map:
                ret += sum_map[prev_sum - k]
            sum_map[prev_sum] += 1
        return ret
```
