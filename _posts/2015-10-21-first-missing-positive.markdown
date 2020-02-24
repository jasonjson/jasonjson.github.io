---
layout: post
title: 41 - First Missing Positive
date: 2015-10-21 02:20:34.000000000 -04:00
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Given an unsorted integer array, find the first missing positive integer.**

``` python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i, num in enumerate(nums):
            if num != i + 1:
                return i + 1
        return len(nums) + 1
```
