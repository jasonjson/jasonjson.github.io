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
**Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.**

```python
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        sums = ret = 0
        sum_map = defaultdict(int)
        for i, num in enumerate(nums):
            sums += num
            if sums == k:
                ret += 1
            if sums - k in sum_map:
                ret += sum_map[sums - k]
            sum_map[sums] += 1
        return ret
```
