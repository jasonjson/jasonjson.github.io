---
layout: post
title: 209 - Minimum Size Subarray Sum
date: 2015-10-21 14:31:53.000000000 -04:00
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum >= s. If there isn't one, return -1 instead.**

``` python
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0

        start = sums = 0
        ret = float("inf")
        for i, num in enumerate(nums):
            sums += num
            while sums >= s:
                ret = min(ret, i - start + 1)
                sums -= nums[start]
                start += 1
        return ret if ret != float("inf") else 0
```
