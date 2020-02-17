---
layout: post
title: 152 - Maximum Product Subarray
date: 2015-10-21 14:30:37.000000000 -04:00
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Find the contiguous subarray within an array (containing at least one number) which has the largest product.**


``` python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        ret = min_val = max_val = nums[0]
        for num in nums[1:]:
            candidates = [min_val * num, max_val * num, num]
            min_val, max_val = min(candidates), max(candidates)
            ret = max(ret, max_val)
        return ret
```
